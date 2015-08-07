import FWCore.ParameterSet.Config as cms

# This step runs over all clusters

# run only if there are high pT jets
from RecoJets.JetProducers.TracksForJets_cff import trackRefsForJets
hiInitialStepTrackRefsForJets = trackRefsForJets.clone(src = cms.InputTag('hiGlobalPrimTracks'))
#from RecoJets.JetProducers.caloJetsForTrk_cff import *

#change this to import Bkg substracted Heavy Ion jets:
from RecoHI.HiJetAlgos.hiCaloJetsForTrk_cff import *

hiJetsForCoreTracking = cms.EDFilter("CandPtrSelector", src = cms.InputTag("akPu4CaloJetsForTrk"), cut = cms.string("pt > 30 && abs(eta) < 2.5"))

# care only at tracks from main PV
hiFirstStepGoodPrimaryVertices = cms.EDFilter("PrimaryVertexObjectFilter",
     filterParams = cms.PSet(
     	     minNdof = cms.double(25.0),
             maxZ = cms.double(15.0),
             maxRho = cms.double(2.0)
     ),
     src=cms.InputTag('hiSelectedVertex')
)

# SEEDING LAYERS
hiJetCoreRegionalStepSeedLayers = cms.EDProducer("SeedingLayersEDProducer",
#    layerList = cms.vstring('BPix1+BPix2', 'BPix1+BPix3', 'BPix2+BPix3', 
#                            'BPix1+FPix1_pos', 'BPix1+FPix1_neg', 
#                            'BPix2+FPix1_pos', 'BPix2+FPix1_neg', 
#                            'FPix1_pos+FPix2_pos', 'FPix1_neg+FPix2_neg',
#                            #'BPix2+TIB1','BPix2+TIB2',
#                            'BPix3+TIB1','BPix3+TIB2'
#),
    layerList = cms.vstring('BPix1+BPix2+BPix3', 
    'BPix1+BPix2+FPix1_pos', 
    'BPix1+BPix2+FPix1_neg', 
    'BPix1+FPix1_pos+FPix2_pos', 
    'BPix1+FPix1_neg+FPix2_neg',
    'BPix1+BPix2+TIB1', 
    'BPix1+BPix3+TIB1', 
    'BPix2+BPix3+TIB1', 
),
    TIB = cms.PSet(
        matchedRecHits = cms.InputTag("siStripMatchedRecHits","matchedRecHit"),
        TTRHBuilder = cms.string('WithTrackAngle'), clusterChargeCut = cms.PSet(refToPSet_ = cms.string('SiStripClusterChargeCutNone'))
    ),
    BPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0027),
        hitErrorRZ = cms.double(0.006),
        TTRHBuilder = cms.string('WithTrackAngle'),
        HitProducer = cms.string('siPixelRecHits'),
        #skipClusters = cms.InputTag('jetCoreRegionalStepClusters')
    ),
    FPix = cms.PSet(
        useErrorsFromParam = cms.bool(True),
        hitErrorRPhi = cms.double(0.0051),
        hitErrorRZ = cms.double(0.0036),
        TTRHBuilder = cms.string('WithTrackAngle'),
        HitProducer = cms.string('siPixelRecHits'),
        #skipClusters = cms.InputTag('jetCoreRegionalStepClusters')
    )
)

# SEEDS
#import RecoTracker.TkSeedGenerator.GlobalSeedsFromPairsWithVertices_cff
#hiJetCoreRegionalStepSeeds = RecoTracker.TkSeedGenerator.GlobalSeedsFromPairsWithVertices_cff.globalSeedsFromPairsWithVertices.clone()
import RecoTracker.TkSeedGenerator.GlobalSeedsFromTriplets_cff
hiJetCoreRegionalStepSeeds = RecoTracker.TkSeedGenerator.GlobalSeedsFromTriplets_cff.globalSeedsFromTriplets.clone()
hiJetCoreRegionalStepSeeds.RegionFactoryPSet = cms.PSet(
      ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),#not so nice to depend on RecoTau...
      RegionPSet = cms.PSet(
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 15. ),
        originHalfLength = cms.double( 0.2 ),
        deltaPhiRegion = cms.double( 0.30 ), 
        deltaEtaRegion = cms.double( 0.30 ), 
        JetSrc = cms.InputTag( "hiJetsForCoreTracking" ),
#       JetSrc = cms.InputTag( "ak5CaloJets" ),
        vertexSrc = cms.InputTag( "hiFirstStepGoodPrimaryVertices" ),
        measurementTrackerName = cms.string( "MeasurementTrackerEvent" ),
        howToUseMeasurementTracker = cms.double( -1.0 )
      )
)
hiJetCoreRegionalStepSeeds.OrderedHitsFactoryPSet.SeedingLayers = 'hiJetCoreRegionalStepSeedLayers'
#hiJetCoreRegionalStepSeeds.OrderedHitsFactoryPSet.maxElement = cms.uint32(100000000) 
hiJetCoreRegionalStepSeeds.SeedComparitorPSet = cms.PSet(
        ComponentName = cms.string('none'),
#PixelClusterShapeSeedComparitor'),
#        FilterAtHelixStage = cms.bool(True),
#        FilterPixelHits = cms.bool(True),
#        FilterStripHits = cms.bool(False),
#       ClusterShapeHitFilterName = cms.string('ClusterShapeHitFilter')
    )
hiJetCoreRegionalStepSeeds.SeedCreatorPSet.forceKinematicWithRegionDirection = cms.bool( True )
hiJetCoreRegionalStepSeeds.ClusterCheckPSet.doClusterCheck = cms.bool( False )

# QUALITY CUTS DURING TRACK BUILDING
import TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff
hiJetCoreRegionalStepTrajectoryFilter = TrackingTools.TrajectoryFiltering.TrajectoryFilter_cff.CkfBaseTrajectoryFilter_block.clone(
    minimumNumberOfHits = 6,
    minPt = 10.0
)

import TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer_cfi
hiJetCoreRegionalStepChi2Est = TrackingTools.KalmanUpdators.Chi2MeasurementEstimatorESProducer_cfi.Chi2MeasurementEstimator.clone(
    ComponentName = cms.string('hiJetCoreRegionalStepChi2Est'),
    nSigma = cms.double(3.0),
    MaxChi2 = cms.double(30.0)
)

# TRACK BUILDING
import RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi
hiJetCoreRegionalStepTrajectoryBuilder = RecoTracker.CkfPattern.GroupedCkfTrajectoryBuilder_cfi.GroupedCkfTrajectoryBuilder.clone(
    MeasurementTrackerName = '',
    trajectoryFilter = cms.PSet(refToPSet_ = cms.string('hiJetCoreRegionalStepTrajectoryFilter')),
    #clustersToSkip = cms.InputTag('jetCoreRegionalStepClusters'),
    maxCand = 50,
    estimator = cms.string('hiJetCoreRegionalStepChi2Est'),
    maxDPhiForLooperReconstruction = cms.double(2.0),
    maxPtForLooperReconstruction = cms.double(0.7)
    )

# MAKING OF TRACK CANDIDATES
import RecoTracker.CkfPattern.CkfTrackCandidates_cfi
hiJetCoreRegionalStepTrackCandidates = RecoTracker.CkfPattern.CkfTrackCandidates_cfi.ckfTrackCandidates.clone(
    src = cms.InputTag('hiJetCoreRegionalStepSeeds'),
    maxSeedsBeforeCleaning = cms.uint32(10000),
    TrajectoryBuilderPSet = cms.PSet( refToPSet_ = cms.string('hiJetCoreRegionalStepTrajectoryBuilder')),
    NavigationSchool = cms.string('SimpleNavigationSchool'),
    ### these two parameters are relevant only for the CachingSeedCleanerBySharedInput
    #numHitsForSeedCleaner = cms.int32(50),
    #onlyPixelHitsForSeedCleaner = cms.bool(True),
)


# TRACK FITTING
import RecoTracker.TrackProducer.TrackProducer_cfi
hiJetCoreRegionalStepTracks = RecoTracker.TrackProducer.TrackProducer_cfi.TrackProducer.clone(
    AlgorithmName = cms.string('hiJetCoreRegionalStep'),
    src = 'hiJetCoreRegionalStepTrackCandidates',
    Fitter = cms.string('FlexibleKFFittingSmoother')
    )

# Final selection
import RecoHI.HiTracking.hiMultiTrackSelector_cfi
hiJetCoreRegionalStepSelector = RecoHI.HiTracking.hiMultiTrackSelector_cfi.hiMultiTrackSelector.clone(
    src='hiJetCoreRegionalStepTracks',
    vertices = cms.InputTag("hiFirstStepGoodPrimaryVertices"),
    trackSelectors= cms.VPSet(
        RecoHI.HiTracking.hiMultiTrackSelector_cfi.hiLooseMTS.clone(
            name = 'hiJetCoreRegionalStepLoose',
            ), #end of pset
        RecoHI.HiTracking.hiMultiTrackSelector_cfi.hiTightMTS.clone(
            name = 'hiJetCoreRegionalStepTight',
            preFilterName = 'hiJetCoreRegionalStepLoose',
            ),
        RecoHI.HiTracking.hiMultiTrackSelector_cfi.hiHighpurityMTS.clone(
            name = 'hiJetCoreRegionalStep',
            preFilterName = 'hiJetCoreRegionalStepTight',
            min_nhits = 14
            ),
        ) #end of vpset
    ) #end of clone

# Final sequence
hiJetCoreRegionalStep = cms.Sequence(
#                                   hiInitialStepTrackRefsForJets*
                                   hiCaloJetsForTrk*hiJetsForCoreTracking*
                                   hiFirstStepGoodPrimaryVertices*
                                   #jetCoreRegionalStepClusters*
                                   hiJetCoreRegionalStepSeedLayers*
                                   hiJetCoreRegionalStepSeeds*
                                   hiJetCoreRegionalStepTrackCandidates*
                                   hiJetCoreRegionalStepTracks*
                                   hiJetCoreRegionalStepSelector)
