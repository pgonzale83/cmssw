

import FWCore.ParameterSet.Config as cms
from PhysicsTools.PatAlgos.patHeavyIonSequences_cff import *
from CmsHi.JetAnalysis.inclusiveJetAnalyzer_cff import *

akVs3PFmatch = patJetGenJetMatch.clone(
    src = cms.InputTag("akVs3PFJets"),
    matched = cms.InputTag("ak3HiGenJets")
    )

akVs3PFparton = patJetPartonMatch.clone(src = cms.InputTag("akVs3PFJets"),
                                                        matched = cms.InputTag("genParticles")
                                                        )

akVs3PFcorr = patJetCorrFactors.clone(
    useNPV = False,
#    primaryVertices = cms.InputTag("hiSelectedVertex"),
    levels   = cms.vstring('L2Relative','L3Absolute'),                                                                
    src = cms.InputTag("akVs3PFJets"),
    payload = "AK3PF_generalTracks"
    )

akVs3PFpatJets = patJets.clone(jetSource = cms.InputTag("akVs3PFJets"),
                                               jetCorrFactorsSource = cms.VInputTag(cms.InputTag("akVs3PFcorr")),
                                               genJetMatch = cms.InputTag("akVs3PFmatch"),
                                               genPartonMatch = cms.InputTag("akVs3PFparton"),
                                               jetIDMap = cms.InputTag("akVs3PFJetID"),
                                               addBTagInfo         = False,
                                               addTagInfos         = False,
                                               addDiscriminators   = False,
                                               addAssociatedTracks = False,
                                               addJetCharge        = False,
                                               addJetID            = False,
                                               getJetMCFlavour     = False,
                                               addGenPartonMatch   = False,
                                               addGenJetMatch      = False,
                                               embedGenJetMatch    = False,
                                               embedGenPartonMatch = False,
                                               embedCaloTowers     = False,
                                               embedPFCandidates = False
				            )

akVs3PFJetAnalyzer = inclusiveJetAnalyzer.clone(jetTag = cms.InputTag("akVs3PFpatJets"),
                                                             genjetTag = 'ak3HiGenJets',
                                                             rParam = 0.3,
                                                             matchJets = cms.untracked.bool(True),
                                                             matchTag = 'akVs3CalopatJets',
                                                             pfCandidateLabel = cms.untracked.InputTag('particleFlowTmp'),
                                                             trackTag = cms.InputTag("generalTracks"),
                                                             fillGenJets = False,
                                                             isMC = False,
                                                             genParticles = cms.untracked.InputTag("genParticles")
                                                             )

akVs3PFJetSequence_mc = cms.Sequence(
						  akVs3PFmatch
                                                  *
                                                  akVs3PFparton
                                                  *
                                                  akVs3PFcorr
                                                  *
                                                  akVs3PFpatJets
                                                  *
                                                  akVs3PFJetAnalyzer
                                                  )

akVs3PFJetSequence_data = cms.Sequence(akVs3PFcorr
                                                    *
                                                    akVs3PFpatJets
                                                    *
                                                    akVs3PFJetAnalyzer
                                                    )

akVs3PFJetSequence = cms.Sequence(akVs3PFJetSequence_data)
