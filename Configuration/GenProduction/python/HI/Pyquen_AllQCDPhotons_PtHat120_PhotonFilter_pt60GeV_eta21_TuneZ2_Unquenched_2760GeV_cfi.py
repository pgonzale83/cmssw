import FWCore.ParameterSet.Config as cms

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
                        particlePt = cms.vdouble(60),
                        particleStatus = cms.vint32(1),
                        partons = cms.vint32(1, 2, 3, 4, 5,  # parton cut is not functioning 
                                             6, 21, 22),
                        partonPt = cms.vdouble(38.5, 38.5, 38.5, 38.5, 38.5,
                                               38.5, 38.5, 38.5),
                        filterType = cms.untracked.string('EcalGenEvtSelectorFrag'),
                        particles = cms.vint32(22),
                        partonStatus = cms.vint32(2, 2, 2, 2, 2,
                                                  2, 2, 1),
                        etaMax = cms.double(2.1),   # Photon eta cut
                        aBeamTarget = cms.double(208.0),
                        comEnergy = cms.double(2760.0),
                        qgpInitialTemperature = cms.double(1.0),
                        doCollisionalEnLoss = cms.bool(False),
                        qgpNumQuarkFlavor = cms.int32(0),
                        qgpProperTimeFormation = cms.double(0.1),
                        numQuarkFlavor = cms.int32(0),
                        hadronFreezoutTemperature = cms.double(0.14),
                        doRadiativeEnLoss = cms.bool(True),
                        backgroundLabel = cms.InputTag("generator"),
                        embeddingMode = cms.bool(True),
                        angularSpectrumSelector = cms.int32(0),
                        doIsospin = cms.bool(True),
                        doQuench = cms.bool(False),
                        cFlag = cms.int32(0),
                        bFixed = cms.double(0.0),
                        bMin = cms.double(0.0),
                        bMax = cms.double(0.0),
                        maxTries = cms.untracked.int32(5000),
                        PythiaParameters = cms.PSet(
    pythiaUpsilonToMuons = cms.vstring('BRAT(1034) = 0 ',
                                       'BRAT(1035) = 1 ',
                                       'BRAT(1036) = 0 ',
                                       'BRAT(1037) = 0 ',
                                       'BRAT(1038) = 0 ',
                                       'BRAT(1039) = 0 ',
                                       'BRAT(1040) = 0 ',
                                       'BRAT(1041) = 0 ',
                                       'BRAT(1042) = 0 ',
                                       'MDME(1034,1) = 0 ',
                                       'MDME(1035,1) = 1 ',
                                       'MDME(1036,1) = 0 ',
                                       'MDME(1037,1) = 0 ',
                                       'MDME(1038,1) = 0 ',
                                       'MDME(1039,1) = 0 ',
                                       'MDME(1040,1) = 0 ',
                                       'MDME(1041,1) = 0 ',
                                       'MDME(1042,1) = 0 '),
    myParameters = cms.vstring(),
    customProcesses = cms.vstring('MSEL=0   ! User processes'),
    ppDefault = cms.vstring('MSEL=1   ! QCD hight pT processes (only jets)',
                            'CKIN(3)=6.',
                            'MSTP(81)=0'),
    pythiaZtoElectrons = cms.vstring('MDME(174,1)=0',
                                     'MDME(175,1)=0',
                                     'MDME(176,1)=0',
                                     'MDME(177,1)=0',
                                     'MDME(178,1)=0',
                                     'MDME(179,1)=0',
                                     'MDME(182,1)=1',
                                     'MDME(183,1)=0',
                                     'MDME(184,1)=0',
                                     'MDME(185,1)=0',
                                     'MDME(186,1)=0',
                                     'MDME(187,1)=0'),
    pythiaZjets = cms.vstring('MSUB(15)=1',
                              'MSUB(30)=1'),
    pythiaUESettingsZ2Tune = cms.vstring(
    'MSTU(21)=1     ! Check on possible errors during program execution',
    'MSTJ(22)=2     ! Decay those unstable particles',
    'PARJ(71)=10 .  ! for which ctau  10 mm',
    'MSTP(33)=0     ! no K factors in hard cross sections',
    'MSTP(2)=1      ! which order running alphaS',
    'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)',
    'MSTP(52)=2     ! work with LHAPDF',
    
    'PARP(82)=1.832 ! pt cutoff for multiparton interactions',
    'PARP(89)=1800. ! sqrts for which PARP82 is set',
    'PARP(90)=0.275 ! Multiple interactions: rescaling power',
    
    'MSTP(95)=6     ! CR (color reconnection parameters)',
    'PARP(77)=1.016 ! CR',
    'PARP(78)=0.538 ! CR',
    
    'PARP(80)=0.1   ! Prob. colored parton from BBR',
    
    'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter',
    'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter',
    
    'PARP(62)=1.025 ! ISR cutoff',
    
    'MSTP(91)=1     ! Gaussian primordial kT',
    'PARP(93)=10.0  ! primordial kT-max',
    
    'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default',
    'MSTP(82)=4     ! Defines the multi-parton model'),
    pythiaZtoMuonsAndElectrons = cms.vstring('MDME(174,1)=0',
                                             'MDME(175,1)=0',
                                             'MDME(176,1)=0',
                                             'MDME(177,1)=0',
                                             'MDME(178,1)=0',
                                             'MDME(179,1)=0',
                                             'MDME(182,1)=1',
                                             'MDME(183,1)=0',
                                             'MDME(184,1)=1',
                                             'MDME(185,1)=0',
                                             'MDME(186,1)=0',
                                             'MDME(187,1)=0'),
    pythiaPromptPhotons = cms.vstring('MSUB(14)=1',
                                      'MSUB(18)=1',
                                      'MSUB(29)=1',
                                      'MSUB(114)=1',
                                      'MSUB(115)=1'),
    pythiaCharmoniumNRQCD = cms.vstring('MSUB(421) = 1',
                                        'MSUB(422) = 1',
                                        'MSUB(423) = 1',
                                        'MSUB(424) = 1',
                                        'MSUB(425) = 1',
                                        'MSUB(426) = 1',
                                        'MSUB(427) = 1',
                                        'MSUB(428) = 1',
                                        'MSUB(429) = 1',
                                        'MSUB(430) = 1',
                                        'MSUB(431) = 1',
                                        'MSUB(432) = 1',
                                        'MSUB(433) = 1',
                                        'MSUB(434) = 1',
                                        'MSUB(435) = 1',
                                        'MSUB(436) = 1',
                                        'MSUB(437) = 1',
                                        'MSUB(438) = 1',
                                        'MSUB(439) = 1'),
    pythiaMuonCandidates = cms.vstring('CKIN(3)=20',
                                           'MSTJ(22)=2',
                                                                                  'PARJ(71)=40.'),
    pythiaQuarkoniaSettings = cms.vstring('PARP(141)=1.16',
                                              'PARP(142)=0.0119',
                                                                                        'PARP(143)=0.01',
                                              'PARP(144)=0.01',
                                              'PARP(145)=0.05',
                                                                                        'PARP(146)=9.28',
                                              'PARP(147)=0.15',
                                              'PARP(148)=0.02',
                                              'PARP(149)=0.02',
                                              'PARP(150)=0.085',
                                              'PARJ(13)=0.60',
                                              'PARJ(14)=0.162',
                                              'PARJ(15)=0.018',
                                              'PARJ(16)=0.054',
                                              'MSTP(145)=0',
                                              'MSTP(146)=0',
                                              'MSTP(147)=0',
                                              'MSTP(148)=1',
                                              'MSTP(149)=1',
                                              'BRAT(861)=0.202',
                                                                                        'BRAT(862)=0.798',
                                                                                        'BRAT(1501)=0.013',
                                                                                        'BRAT(1502)=0.987',
                                                                                        'BRAT(1555)=0.356',
                                                                                        'BRAT(1556)=0.644'),
    pythiaBottomoniumNRQCD = cms.vstring('MSUB(461) = 1',
                                         'MSUB(462) = 1',
                                         'MSUB(463) = 1',
                                         'MSUB(464) = 1',
                                         'MSUB(465) = 1',
                                         'MSUB(466) = 1',
                                         'MSUB(467) = 1',
                                         'MSUB(468) = 1',
                                         'MSUB(469) = 1',
                                         'MSUB(470) = 1',
                                         'MSUB(471) = 1',
                                         'MSUB(472) = 1',
                                         'MSUB(473) = 1',
                                         'MSUB(474) = 1',
                                         'MSUB(475) = 1',
                                         'MSUB(476) = 1',
                                         'MSUB(477) = 1',
                                         'MSUB(478) = 1',
                                         'MSUB(479) = 1'),
    pythiaWeakBosons = cms.vstring('MSUB(1)=1',
                                   'MSUB(2)=1'),
    pythiaJets = cms.vstring('MSUB(11)=1',
                             'MSUB(12)=1',
                             'MSUB(13)=1',
                             'MSUB(28)=1',
                             'MSUB(53)=1',
                             'MSUB(68)=1'),
    pythiaZtoMuons = cms.vstring('MDME(174,1)=0',
                                 'MDME(175,1)=0',
                                        'MDME(176,1)=0',
                                        'MDME(177,1)=0',
                                        'MDME(178,1)=0',
                                        'MDME(179,1)=0',
                                        'MDME(182,1)=0',
                                        'MDME(183,1)=0',
                                        'MDME(184,1)=1',
                                        'MDME(185,1)=0',
                                        'MDME(186,1)=0',
                                        'MDME(187,1)=0'),
    hydjetPythiaDefault = cms.vstring('MSEL=0   ! user processes',
                                      'CKIN(3)=6.',
                                      'MSTP(81)=0'),
    ppJets = cms.vstring('MSEL=1   ! QCD hight pT processes'),
    pythiaHirootDefault = cms.vstring('MSEL=0',
                                      'MSTU(21)=1',
                                      'PARU(14)=1.',
                                      'MSTP(81)=0',
                                      'PMAS(5,1)=4.8',
                                      'PMAS(6,1)=175.0',
                                      'CKIN(3)=7.',
                                      'MSTJ(22)=2',
                                      'PARJ(71)=10.',
                                      'PARP(67)=1.',
                                      'PARP(82)=1.9',
                                      'PARP(85)=0.33',
                                      'PARP(86)=0.66',
                                      'PARP(89)=1000.',
                                      'PARP(91)=1.0',
                                      'MSTJ(11)=3',
                                      'MSTJ(22)=2'),
    pythiaJpsiToMuons = cms.vstring('BRAT(858) = 0 ',
                                    'BRAT(859) = 1 ',
                                    'BRAT(860) = 0 ',
                                    'MDME(858,1) = 0 ',
                                    'MDME(859,1) = 1 ',
                                    'MDME(860,1) = 0 '),
    # Don't use    EnhanceFragPhoton = cms.vstring('MSTJ(41) = 10 ',
    #                                    'PARJ(84) = 20.0 '),
    allQCDPhotonChannel = cms.vstring(    'MSUB(11)=1', # q+q->q+q
                                          'MSUB(12)=1', # q+qbar->q+qbar
                                          'MSUB(13)=1', # q+qbar->g+g
                                          'MSUB(28)=1', # q+g->q+g
                                          'MSUB(53)=1', # g+g->q+qbar
                                          'MSUB(68)=1', # g+g->g+g
                                          # Leading order photons
                                          'MSUB(14)=1', # q+qbar->g+gamma
                                          'MSUB(18)=1', # q+qbar->gamma+gamma
                                          'MSUB(29)=1', # q+g->q+gamma
                                          'MSUB(114)=1', # g+g->gamma+gamma
                                          'MSUB(115)=1' # g+g->g+gamma
                                          ),
    
    parameterSets = cms.vstring('pythiaUESettingsZ2Tune',
                                'customProcesses',
                                'allQCDPhotonChannel',
                                'kinematics'),
    kinematics = cms.vstring('CKIN(3)=120',
                             'CKIN(4)=9999'
                             )
    )
                        )



