

import FWCore.ParameterSet.Config as cms
from HeavyIonsAnalysis.JetAnalysis.patHeavyIonSequences_cff import patJetGenJetMatch, patJetPartonMatch, patJetCorrFactors, patJets
from HeavyIonsAnalysis.JetAnalysis.inclusiveJetAnalyzer_cff import *
from HeavyIonsAnalysis.JetAnalysis.bTaggers_cff import *
from RecoJets.JetProducers.JetIDParams_cfi import *
from RecoJets.JetProducers.nJettinessAdder_cfi import Njettiness

akPu3Calomatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akPu3CaloJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPu3CalomatchGroomed = patJetGenJetMatch.clone(
    src = cms.InputTag("ak3GenJets"),
    matched = cms.InputTag("ak3GenJets"),
    resolveByMatchQuality = cms.bool(False),
    maxDeltaR = 0.3
    )

akPu3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3CaloJets")
                                                        )

akPu3Calocorr = patJetCorrFactors.clone(
    useNPV = cms.bool(False),
    useRho = cms.bool(False),
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),
    src = cms.InputTag("akPu3CaloJets"),
    payload = "AKPu3Calo_offline"
    )

akPu3CaloJetID= cms.EDProducer('JetIDProducer', JetIDParams, src = cms.InputTag('akPu3CaloJets'))

#akPu3Caloclean   = heavyIonCleanedGenJets.clone(src = cms.InputTag('ak3GenJets'))

akPu3CalobTagger = bTaggers("akPu3Calo",0.3,True,False)

#create objects locally since they dont load properly otherwise
#akPu3Calomatch = akPu3CalobTagger.match
akPu3Caloparton = patJetPartonMatch.clone(src = cms.InputTag("akPu3CaloJets"), matched = cms.InputTag("genParticles"))
akPu3CaloPatJetFlavourAssociationLegacy = akPu3CalobTagger.PatJetFlavourAssociationLegacy
akPu3CaloPatJetPartons = akPu3CalobTagger.PatJetPartons
akPu3CaloJetTracksAssociatorAtVertex = akPu3CalobTagger.JetTracksAssociatorAtVertex
akPu3CaloJetTracksAssociatorAtVertex.tracks = cms.InputTag("highPurityTracks")
akPu3CaloSimpleSecondaryVertexHighEffBJetTags = akPu3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu3CaloSimpleSecondaryVertexHighPurBJetTags = akPu3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu3CaloCombinedSecondaryVertexBJetTags = akPu3CalobTagger.CombinedSecondaryVertexBJetTags
akPu3CaloCombinedSecondaryVertexV2BJetTags = akPu3CalobTagger.CombinedSecondaryVertexV2BJetTags
akPu3CaloJetBProbabilityBJetTags = akPu3CalobTagger.JetBProbabilityBJetTags
akPu3CaloSoftPFMuonByPtBJetTags = akPu3CalobTagger.SoftPFMuonByPtBJetTags
akPu3CaloSoftPFMuonByIP3dBJetTags = akPu3CalobTagger.SoftPFMuonByIP3dBJetTags
akPu3CaloTrackCountingHighEffBJetTags = akPu3CalobTagger.TrackCountingHighEffBJetTags
akPu3CaloTrackCountingHighPurBJetTags = akPu3CalobTagger.TrackCountingHighPurBJetTags
akPu3CaloPatJetPartonAssociationLegacy = akPu3CalobTagger.PatJetPartonAssociationLegacy

akPu3CaloImpactParameterTagInfos = akPu3CalobTagger.ImpactParameterTagInfos
akPu3CaloImpactParameterTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3CaloJetProbabilityBJetTags = akPu3CalobTagger.JetProbabilityBJetTags

akPu3CaloSecondaryVertexTagInfos = akPu3CalobTagger.SecondaryVertexTagInfos
akPu3CaloSimpleSecondaryVertexHighEffBJetTags = akPu3CalobTagger.SimpleSecondaryVertexHighEffBJetTags
akPu3CaloSimpleSecondaryVertexHighPurBJetTags = akPu3CalobTagger.SimpleSecondaryVertexHighPurBJetTags
akPu3CaloCombinedSecondaryVertexBJetTags = akPu3CalobTagger.CombinedSecondaryVertexBJetTags
akPu3CaloCombinedSecondaryVertexV2BJetTags = akPu3CalobTagger.CombinedSecondaryVertexV2BJetTags

akPu3CaloSecondaryVertexNegativeTagInfos = akPu3CalobTagger.SecondaryVertexNegativeTagInfos
akPu3CaloNegativeSimpleSecondaryVertexHighEffBJetTags = akPu3CalobTagger.NegativeSimpleSecondaryVertexHighEffBJetTags
akPu3CaloNegativeSimpleSecondaryVertexHighPurBJetTags = akPu3CalobTagger.NegativeSimpleSecondaryVertexHighPurBJetTags
akPu3CaloNegativeCombinedSecondaryVertexBJetTags = akPu3CalobTagger.NegativeCombinedSecondaryVertexBJetTags
akPu3CaloPositiveCombinedSecondaryVertexBJetTags = akPu3CalobTagger.PositiveCombinedSecondaryVertexBJetTags
akPu3CaloNegativeCombinedSecondaryVertexV2BJetTags = akPu3CalobTagger.NegativeCombinedSecondaryVertexV2BJetTags
akPu3CaloPositiveCombinedSecondaryVertexV2BJetTags = akPu3CalobTagger.PositiveCombinedSecondaryVertexV2BJetTags

akPu3CaloSoftPFMuonsTagInfos = akPu3CalobTagger.SoftPFMuonsTagInfos
akPu3CaloSoftPFMuonsTagInfos.primaryVertex = cms.InputTag("offlinePrimaryVertices")
akPu3CaloSoftPFMuonBJetTags = akPu3CalobTagger.SoftPFMuonBJetTags
akPu3CaloSoftPFMuonByIP3dBJetTags = akPu3CalobTagger.SoftPFMuonByIP3dBJetTags
akPu3CaloSoftPFMuonByPtBJetTags = akPu3CalobTagger.SoftPFMuonByPtBJetTags
akPu3CaloNegativeSoftPFMuonByPtBJetTags = akPu3CalobTagger.NegativeSoftPFMuonByPtBJetTags
akPu3CaloPositiveSoftPFMuonByPtBJetTags = akPu3CalobTagger.PositiveSoftPFMuonByPtBJetTags
akPu3CaloPatJetFlavourIdLegacy = cms.Sequence(akPu3CaloPatJetPartonAssociationLegacy*akPu3CaloPatJetFlavourAssociationLegacy)
#Not working with our PU sub
akPu3CaloPatJetFlavourAssociation = akPu3CalobTagger.PatJetFlavourAssociation
akPu3CaloPatJetFlavourId = cms.Sequence(akPu3CaloPatJetPartons*akPu3CaloPatJetFlavourAssociation)

#adding the subjet taggers
#SUBJETDUMMY_akPu3CaloSubjetImpactParameterTagInfos = akPu3CalobTagger.SubjetImpactParameterTagInfos
#SUBJETDUMMY_akPu3CaloSubjetJetProbabilityBJetTags = akPu3CalobTagger.SubjetJetProbabilityBJetTags
#SUBJETDUMMY_akPu3CaloSubjetSecondaryVertexTagInfos = akPu3CalobTagger.SubjetSecondaryVertexTagInfos
#SUBJETDUMMY_akPu3CaloSubjetSecondaryVertexNegativeTagInfos = akPu3CalobTagger.SubjetSecondaryVertexNegativeTagInfos
#SUBJETDUMMY_akPu3CaloSubjetJetTracksAssociatorAtVertex = akPu3CalobTagger.SubjetJetTracksAssociatorAtVertex
#SUBJETDUMMY_akPu3CaloCombinedSubjetSecondaryVertexBJetTags = akPu3CalobTagger.CombinedSubjetSecondaryVertexBJetTags
#SUBJETDUMMY_akPu3CaloCombinedSubjetSecondaryVertexV2BJetTags = akPu3CalobTagger.CombinedSubjetSecondaryVertexV2BJetTags
#SUBJETDUMMY_akPu3CaloCombinedSubjetNegativeSecondaryVertexV2BJetTags = akPu3CalobTagger.CombinedSubjetNegativeSecondaryVertexV2BJetTags

akPu3CaloJetBtaggingIP       = cms.Sequence(akPu3CaloImpactParameterTagInfos *
            (akPu3CaloTrackCountingHighEffBJetTags +
             akPu3CaloTrackCountingHighPurBJetTags +
             akPu3CaloJetProbabilityBJetTags +
             akPu3CaloJetBProbabilityBJetTags 
            )
            )

akPu3CaloJetBtaggingSV = cms.Sequence(akPu3CaloImpactParameterTagInfos
            *
            akPu3CaloSecondaryVertexTagInfos
            * (akPu3CaloSimpleSecondaryVertexHighEffBJetTags+
                akPu3CaloSimpleSecondaryVertexHighPurBJetTags+
                akPu3CaloCombinedSecondaryVertexBJetTags+
                akPu3CaloCombinedSecondaryVertexV2BJetTags
              )
            )

akPu3CaloJetBtaggingNegSV = cms.Sequence(akPu3CaloImpactParameterTagInfos
            *
            akPu3CaloSecondaryVertexNegativeTagInfos
            * (akPu3CaloNegativeSimpleSecondaryVertexHighEffBJetTags+
                akPu3CaloNegativeSimpleSecondaryVertexHighPurBJetTags+
                akPu3CaloNegativeCombinedSecondaryVertexBJetTags+
                akPu3CaloPositiveCombinedSecondaryVertexBJetTags+
                akPu3CaloNegativeCombinedSecondaryVertexV2BJetTags+
                akPu3CaloPositiveCombinedSecondaryVertexV2BJetTags
              )
            )

akPu3CaloJetBtaggingMu = cms.Sequence(akPu3CaloSoftPFMuonsTagInfos * (akPu3CaloSoftPFMuonBJetTags
                +
                akPu3CaloSoftPFMuonByIP3dBJetTags
                +
                akPu3CaloSoftPFMuonByPtBJetTags
                +
                akPu3CaloNegativeSoftPFMuonByPtBJetTags
                +
                akPu3CaloPositiveSoftPFMuonByPtBJetTags
              )
            )

akPu3CaloJetBtagging = cms.Sequence(akPu3CaloJetBtaggingIP
            *akPu3CaloJetBtaggingSV
            *akPu3CaloJetBtaggingNegSV
#            *akPu3CaloJetBtaggingMu
            )

akPu3CalopatJetsWithBtagging = patJets.clone(jetSource = cms.InputTag("akPu3CaloJets"),
        genJetMatch          = cms.InputTag("akPu3Calomatch"),
        genPartonMatch       = cms.InputTag("akPu3Caloparton"),
        jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akPu3Calocorr")),
        #JetPartonMapSource   = cms.InputTag("akPu3CaloPatJetFlavourAssociationLegacy"),
        JetPartonMapSource   = cms.InputTag("akPu3CaloPatJetFlavourAssociation"),
	JetFlavourInfoSource   = cms.InputTag("akPu3CaloPatJetFlavourAssociation"),
        trackAssociationSource = cms.InputTag("akPu3CaloJetTracksAssociatorAtVertex"),
	useLegacyJetMCFlavour = False,
        discriminatorSources = cms.VInputTag(cms.InputTag("akPu3CaloSimpleSecondaryVertexHighEffBJetTags"),
            cms.InputTag("akPu3CaloSimpleSecondaryVertexHighPurBJetTags"),
            cms.InputTag("akPu3CaloCombinedSecondaryVertexBJetTags"),
            cms.InputTag("akPu3CaloCombinedSecondaryVertexV2BJetTags"),
            cms.InputTag("akPu3CaloJetBProbabilityBJetTags"),
            cms.InputTag("akPu3CaloJetProbabilityBJetTags"),
            #cms.InputTag("akPu3CaloSoftPFMuonByPtBJetTags"),
            #cms.InputTag("akPu3CaloSoftPFMuonByIP3dBJetTags"),
            cms.InputTag("akPu3CaloTrackCountingHighEffBJetTags"),
            cms.InputTag("akPu3CaloTrackCountingHighPurBJetTags"),
            ),
        jetIDMap = cms.InputTag("akPu3CaloJetID"),
        addBTagInfo = True,
        addTagInfos = True,
        addDiscriminators = True,
        addAssociatedTracks = True,
        addJetCharge = False,
        addJetID = False,
        getJetMCFlavour = False,
        addGenPartonMatch = False,
        addGenJetMatch = False,
        embedGenJetMatch = False,
        embedGenPartonMatch = False,
        # embedCaloTowers = False,
        # embedPFCandidates = True
        )

akPu3CaloNjettiness = Njettiness.clone(
		    src = cms.InputTag("akPu3CaloJets"),
           	    R0  = cms.double( 0.3)
)
akPu3CalopatJetsWithBtagging.userData.userFloats.src += ['akPu3CaloNjettiness:tau1','akPu3CaloNjettiness:tau2','akPu3CaloNjettiness:tau3']

akPu3CaloJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akPu3CalopatJetsWithBtagging"),
                                                             genjetTag = 'ak3GenJets',
                                                             rParam = 0.3,
                                                             matchJets = cms.untracked.bool(False),
                                                             matchTag = 'patJetsWithBtagging',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlow'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
							     doSubEvent = False,
                                                             useHepMC = cms.untracked.bool(False),
							     genParticles = cms.untracked.InputTag("genParticles"),
							     eventInfoTag = cms.InputTag("generator"),
                                                             doLifeTimeTagging = cms.untracked.bool(True),
                                                             doLifeTimeTaggingExtras = cms.untracked.bool(False),
                                                             bTagJetName = cms.untracked.string("akPu3Calo"),
                                                             jetName = cms.untracked.string("akPu3Calo"),
                                                             genPtMin = cms.untracked.double(5),
                                                             hltTrgResults = cms.untracked.string('TriggerResults::'+'HISIGNAL'),
							     doTower = cms.untracked.bool(False),
							     doSubJets = cms.untracked.bool(False),
                                                             doGenSubJets = cms.untracked.bool(False),     
                                                             subjetGenTag = cms.untracked.InputTag("ak3GenJets"),
							     doExtendedFlavorTagging = cms.untracked.bool(False),
							     jetFlavourInfos = cms.InputTag("akPu3CaloPatJetFlavourAssociation"),
							     subjetFlavourInfos = cms.InputTag("akPu3CaloPatJetFlavourAssociation","SubJets"),
							     groomedJets = cms.InputTag("akPu3CaloJets"),
							     isPythia6 = cms.untracked.bool(False),
                                                             doGenTaus = False
                                                            )

akPu3CaloJetSequence_mc = cms.Sequence(
                                                  #akPu3Caloclean
                                                  #*
                                                  akPu3Calomatch
                                                  #*
                                                  #akPu3CalomatchGroomed
                                                  *
                                                  akPu3Caloparton
                                                  *
                                                  akPu3Calocorr
                                                  *
                                                  #akPu3CaloJetID
                                                  #*
                                                  #akPu3CaloPatJetFlavourIdLegacy  # works for PbPb
                                                  #*
			                          akPu3CaloPatJetFlavourId  # doesn't work for PbPb yet
                                                  *
                                                  akPu3CaloJetTracksAssociatorAtVertex
                                                  *
                                                  akPu3CaloJetBtagging
                                                  *
                                                  akPu3CaloNjettiness #No constituents for calo jets in pp. Must be removed for pp calo jets but I'm not sure how to do this transparently (Marta)
                                                  *
                                                  akPu3CalopatJetsWithBtagging
                                                  *
                                                  akPu3CaloJetAnalyzer
                                                  )

akPu3CaloJetSequence_data = cms.Sequence(akPu3Calocorr
                                                    *
                                                    #akPu3CaloJetID
                                                    #*
                                                    akPu3CaloJetTracksAssociatorAtVertex
                                                    *
                                                    akPu3CaloJetBtagging
                                                    *
                                                    akPu3CaloNjettiness 
                                                    *
                                                    akPu3CalopatJetsWithBtagging
                                                    *
                                                    akPu3CaloJetAnalyzer
                                                    )

akPu3CaloJetSequence_jec = cms.Sequence(akPu3CaloJetSequence_mc)
akPu3CaloJetSequence_mb = cms.Sequence(akPu3CaloJetSequence_mc)

akPu3CaloJetSequence = cms.Sequence(akPu3CaloJetSequence_data)
