# /cdaq/physics/Run2010/v8.1/HLT/V1 (CMSSW_3_8_1_HLT16)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "HLT" )

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string( '/cdaq/physics/Run2010/v8.1/HLT/V1' )
)

process.options = cms.PSet(
  Rethrow = cms.untracked.vstring( "ProductNotFound", "TooManyProducts", "TooFewProducts" )
)

process.streams = cms.PSet(
  A = cms.vstring( 'BTau',
    'Commissioning',
    'Cosmics',
    'EGMonitor',
    'Electron',
    'HcalHPDNoise',
    'HcalNZS',
    'Jet',
    'JetMETTauMonitor',
    'METFwd',
    'MinimumBias',
    'Mu',
    'MuMonitor',
    'MuOnia',
    'MultiJet',
    'Photon' ),
  ALCAP0 = cms.vstring( 'AlCaP0' ),
  ALCAPHISYM = cms.vstring( 'AlCaPhiSymEcal' ),
  Calibration = cms.vstring( 'TestEnables' ),
  DQM = cms.vstring( 'OnlineMonitor' ),
  EcalCalibration = cms.vstring( 'EcalLaser' ),
  Express = cms.vstring( 'ExpressPhysics' ),
  HLTDQM = cms.vstring( 'OnlineHltMonitor' ),
  HLTDQMResults = cms.vstring( 'OnlineHltResults' ),
  HLTMON = cms.vstring( 'OfflineMonitor' ),
  NanoDST = cms.vstring( 'L1Accept' ),
  OnlineErrors = cms.vstring( 'FEDMonitor',
    'LogMonitor' ),
  RPCMON = cms.vstring( 'RPCMonitor' )
)

process.datasets = cms.PSet(
  AlCaP0 = cms.vstring( 'AlCa_EcalEta',
    'AlCa_EcalPi0' ),
  AlCaPhiSymEcal = cms.vstring( 'AlCa_EcalPhiSym' ),
  BTau = cms.vstring( 'HLT_BTagMu_DiJet10U_v1',
    'HLT_BTagMu_DiJet20U_Mu5_v1',
    'HLT_BTagMu_DiJet20U_v1',
    'HLT_DoubleIsoTau15_OneLeg_Trk5',
    'HLT_DoubleIsoTau15_Trk5',
    'HLT_SingleIsoTau20_Trk15_MET20',
    'HLT_SingleIsoTau20_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_v2' ),
  Commissioning = cms.vstring( 'HLT_Activity_CSC',
    'HLT_Activity_DT',
    'HLT_Activity_DT_Tuned',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v2',
    'HLT_L1_BptxXOR_BscMinBiasOR',
    'HLT_MultiVertex6',
    'HLT_MultiVertex8_L1ETT60' ),
  Cosmics = cms.vstring( 'HLT_L1MuOpen_AntiBPTX',
    'HLT_L1Tech_BSC_halo',
    'HLT_L2Mu0_NoVertex',
    'HLT_RPCBarrelCosmics',
    'HLT_TrackerCosmics' ),
  EGMonitor = cms.vstring( 'HLT_Activity_Ecal_SC17',
    'HLT_Activity_Ecal_SC7',
    'HLT_DoubleEle4_SW_eeRes_L1R',
    'HLT_Ele10_SW_L1R',
    'HLT_Ele12_SW_TightEleId_L1R',
    'HLT_Ele12_SW_TighterEleId_L1R_v1',
    'HLT_Ele17_SW_L1R',
    'HLT_L1SingleEG2',
    'HLT_L1SingleEG8',
    'HLT_Photon10_Cleaned_L1R',
    'HLT_Photon15_Cleaned_L1R',
    'HLT_Photon20_NoHE_L1R',
    'HLT_Photon50_NoHE_L1R' ),
  EcalLaser = cms.vstring( 'HLT_EcalCalibration' ),
  Electron = cms.vstring( 'HLT_DoubleEle15_SW_L1R_v1',
    'HLT_Ele10_MET45_v1',
    'HLT_Ele12_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1',
    'HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1',
    'HLT_Ele17_SW_TightEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TightEleId_L1R',
    'HLT_Ele17_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TighterEleId_L1R_v1',
    'HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1' ),
  ExpressPhysics = cms.vstring( 'HLT_DoubleMu3_v2',
    'HLT_Jet140U_v1',
    'HLT_L1Tech_BSC_minBias_OR',
    'HLT_MET100_v2',
    'HLT_Mu15_v1',
    'HLT_Photon70_NoHE_Cleaned_L1R_v1',
    'HLT_TrackerCosmics',
    'HLT_ZeroBias' ),
  FEDMonitor = cms.vstring( 'HLT_DTErrors' ),
  HcalHPDNoise = cms.vstring( 'HLT_GlobalRunHPDNoise',
    'HLT_TechTrigHCALNoise' ),
  HcalNZS = cms.vstring( 'HLT_HcalNZS',
    'HLT_HcalPhiSym' ),
  Jet = cms.vstring( 'HLT_DiJetAve100U_v1',
    'HLT_DiJetAve15U',
    'HLT_DiJetAve30U',
    'HLT_DiJetAve50U',
    'HLT_DiJetAve70U_v2',
    'HLT_Jet100U_v2',
    'HLT_Jet140U_v1',
    'HLT_Jet15U',
    'HLT_Jet15U_HcalNoiseFiltered',
    'HLT_Jet30U',
    'HLT_Jet50U',
    'HLT_Jet70U_v2' ),
  JetMETTauMonitor = cms.vstring( 'HLT_HT100U',
    'HLT_HT120U',
    'HLT_HT50U_v1',
    'HLT_L1ETT100',
    'HLT_L1ETT140_v1',
    'HLT_L1Jet10U',
    'HLT_L1Jet6U',
    'HLT_L1MET20',
    'HLT_QuadJet15U_v2' ),
  L1Accept = cms.vstring( 'HLTriggerFinalPath' ),
  LogMonitor = cms.vstring( 'HLT_LogMonitor' ),
  METFwd = cms.vstring( 'HLT_DoubleJet15U_ForwardBackward',
    'HLT_DoubleJet25U_ForwardBackward',
    'HLT_MET100_v2',
    'HLT_MET45',
    'HLT_MET45_HT100U_v1',
    'HLT_MET45_HT120U_v1',
    'HLT_MET65',
    'HLT_MET80_v1' ),
  MinimumBias = cms.vstring( 'HLT_L1Tech_BSC_HighMultiplicity',
    'HLT_L1Tech_BSC_halo_forPhysicsBackground',
    'HLT_L1Tech_BSC_minBias',
    'HLT_L1Tech_BSC_minBias_OR',
    'HLT_L1Tech_HCAL_HF',
    'HLT_L1Tech_RPC_TTU_RBst1_collisions',
    'HLT_L1_BPTX',
    'HLT_L1_BPTX_MinusOnly',
    'HLT_L1_BPTX_PlusOnly',
    'HLT_MinBiasPixel_SingleTrack',
    'HLT_PixelTracks_Multiplicity100',
    'HLT_PixelTracks_Multiplicity70',
    'HLT_PixelTracks_Multiplicity85',
    'HLT_Random',
    'HLT_StoppedHSCP20_v3',
    'HLT_StoppedHSCP35_v3',
    'HLT_ZeroBias',
    'HLT_ZeroBiasPixel_SingleTrack' ),
  Mu = cms.vstring( 'HLT_DoubleMu3_v2',
    'HLT_DoubleMu5_v1',
    'HLT_IsoMu11_v1',
    'HLT_IsoMu9',
    'HLT_L2DoubleMu20_NoVertex_v1',
    'HLT_Mu11',
    'HLT_Mu13_v1',
    'HLT_Mu15_v1',
    'HLT_Mu20_NoVertex',
    'HLT_Mu5_Ele5_v1',
    'HLT_Mu5_Ele9_v1',
    'HLT_Mu5_HT50U_v1',
    'HLT_Mu5_HT70U_v1',
    'HLT_Mu5_Jet35U_v1',
    'HLT_Mu5_Jet50U_v2',
    'HLT_Mu5_MET45_v1',
    'HLT_Mu5_Photon11_Cleaned_L1R_v1',
    'HLT_Mu9' ),
  MuMonitor = cms.vstring( 'HLT_DoubleMu0',
    'HLT_L1DoubleMuOpen',
    'HLT_L1Mu20',
    'HLT_L1Mu7_v1',
    'HLT_L1MuOpen',
    'HLT_L1MuOpen_DT',
    'HLT_L2DoubleMu0',
    'HLT_L2Mu30_v1',
    'HLT_L2Mu7_v1',
    'HLT_Mu3',
    'HLT_Mu5',
    'HLT_Mu7' ),
  MuOnia = cms.vstring( 'HLT_DoubleMu0_Quarkonium_LS_v1',
    'HLT_DoubleMu0_Quarkonium_v1',
    'HLT_Mu0_TkMu0_OST_Jpsi',
    'HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1',
    'HLT_Mu3_TkMu0_OST_Jpsi',
    'HLT_Mu3_Track3_Jpsi',
    'HLT_Mu3_Track5_Jpsi_v1',
    'HLT_Mu5_L2Mu0',
    'HLT_Mu5_TkMu0_OST_Jpsi',
    'HLT_Mu5_Track0_Jpsi' ),
  MultiJet = cms.vstring( 'HLT_EcalOnly_SumEt160_v2',
    'HLT_ExclDiJet30U_HFAND_v1',
    'HLT_ExclDiJet30U_HFOR_v1',
    'HLT_HT140U',
    'HLT_HT140U_Eta3_v1',
    'HLT_HT160U_v1',
    'HLT_HT200U_v1',
    'HLT_QuadJet20U_v2',
    'HLT_QuadJet25U_v2' ),
  OfflineMonitor = cms.vstring( 'AlCa_EcalEta',
    'AlCa_EcalPhiSym',
    'AlCa_EcalPi0',
    'AlCa_RPCMuonNoHits',
    'AlCa_RPCMuonNoTriggers',
    'AlCa_RPCMuonNormalisation',
    'HLT_Activity_CSC',
    'HLT_Activity_DT',
    'HLT_Activity_DT_Tuned',
    'HLT_Activity_Ecal_SC17',
    'HLT_Activity_Ecal_SC7',
    'HLT_BTagMu_DiJet10U_v1',
    'HLT_BTagMu_DiJet20U_Mu5_v1',
    'HLT_BTagMu_DiJet20U_v1',
    'HLT_DTErrors',
    'HLT_DiJetAve100U_v1',
    'HLT_DiJetAve15U',
    'HLT_DiJetAve30U',
    'HLT_DiJetAve50U',
    'HLT_DiJetAve70U_v2',
    'HLT_DoubleEle15_SW_L1R_v1',
    'HLT_DoubleEle4_SW_eeRes_L1R',
    'HLT_DoubleIsoTau15_OneLeg_Trk5',
    'HLT_DoubleIsoTau15_Trk5',
    'HLT_DoubleJet15U_ForwardBackward',
    'HLT_DoubleJet25U_ForwardBackward',
    'HLT_DoubleMu0_Quarkonium_LS_v1',
    'HLT_DoubleMu0_Quarkonium_v1',
    'HLT_DoubleMu3_v2',
    'HLT_DoubleMu5_v1',
    'HLT_DoublePhoton17_L1R',
    'HLT_DoublePhoton5_CEP_L1R',
    'HLT_EcalOnly_SumEt160_v2',
    'HLT_Ele10_MET45_v1',
    'HLT_Ele10_SW_L1R',
    'HLT_Ele12_SW_TightEleId_L1R',
    'HLT_Ele12_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele12_SW_TighterEleId_L1R_v1',
    'HLT_Ele17_SW_L1R',
    'HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1',
    'HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1',
    'HLT_Ele17_SW_TightEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TightEleId_L1R',
    'HLT_Ele17_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TighterEleId_L1R_v1',
    'HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_ExclDiJet30U_HFAND_v1',
    'HLT_ExclDiJet30U_HFOR_v1',
    'HLT_GlobalRunHPDNoise',
    'HLT_HT100U',
    'HLT_HT120U',
    'HLT_HT140U',
    'HLT_HT140U_Eta3_v1',
    'HLT_HT160U_v1',
    'HLT_HT200U_v1',
    'HLT_HT50U_v1',
    'HLT_HcalNZS',
    'HLT_HcalPhiSym',
    'HLT_IsoMu11_v1',
    'HLT_IsoMu9',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v2',
    'HLT_Jet100U_v2',
    'HLT_Jet140U_v1',
    'HLT_Jet15U',
    'HLT_Jet15U_HcalNoiseFiltered',
    'HLT_Jet30U',
    'HLT_Jet50U',
    'HLT_Jet70U_v2',
    'HLT_L1DoubleMuOpen',
    'HLT_L1ETT100',
    'HLT_L1ETT140_v1',
    'HLT_L1Jet10U',
    'HLT_L1Jet6U',
    'HLT_L1MET20',
    'HLT_L1Mu20',
    'HLT_L1Mu7_v1',
    'HLT_L1MuOpen',
    'HLT_L1MuOpen_AntiBPTX',
    'HLT_L1MuOpen_DT',
    'HLT_L1SingleEG2',
    'HLT_L1SingleEG8',
    'HLT_L1Tech_BSC_HighMultiplicity',
    'HLT_L1Tech_BSC_halo',
    'HLT_L1Tech_BSC_halo_forPhysicsBackground',
    'HLT_L1Tech_BSC_minBias',
    'HLT_L1Tech_BSC_minBias_OR',
    'HLT_L1Tech_HCAL_HF',
    'HLT_L1Tech_RPC_TTU_RBst1_collisions',
    'HLT_L1_BPTX',
    'HLT_L1_BPTX_MinusOnly',
    'HLT_L1_BPTX_PlusOnly',
    'HLT_L1_BptxXOR_BscMinBiasOR',
    'HLT_L2DoubleMu0',
    'HLT_L2DoubleMu20_NoVertex_v1',
    'HLT_L2Mu0_NoVertex',
    'HLT_L2Mu30_v1',
    'HLT_L2Mu7_v1',
    'HLT_LogMonitor',
    'HLT_MET100_v2',
    'HLT_MET45',
    'HLT_MET45_HT100U_v1',
    'HLT_MET45_HT120U_v1',
    'HLT_MET65',
    'HLT_MET80_v1',
    'HLT_MinBiasPixel_SingleTrack',
    'HLT_Mu0_TkMu0_OST_Jpsi',
    'HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1',
    'HLT_Mu11',
    'HLT_Mu13_v1',
    'HLT_Mu15_v1',
    'HLT_Mu20_NoVertex',
    'HLT_Mu3',
    'HLT_Mu3_TkMu0_OST_Jpsi',
    'HLT_Mu3_Track3_Jpsi',
    'HLT_Mu3_Track5_Jpsi_v1',
    'HLT_Mu5',
    'HLT_Mu5_Ele5_v1',
    'HLT_Mu5_Ele9_v1',
    'HLT_Mu5_HT50U_v1',
    'HLT_Mu5_HT70U_v1',
    'HLT_Mu5_Jet35U_v1',
    'HLT_Mu5_Jet50U_v2',
    'HLT_Mu5_L2Mu0',
    'HLT_Mu5_MET45_v1',
    'HLT_Mu5_Photon11_Cleaned_L1R_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi',
    'HLT_Mu5_Track0_Jpsi',
    'HLT_Mu7',
    'HLT_Mu9',
    'HLT_MultiVertex6',
    'HLT_MultiVertex8_L1ETT60',
    'HLT_Photon100_NoHE_Cleaned_L1R_v1',
    'HLT_Photon10_Cleaned_L1R',
    'HLT_Photon15_Cleaned_L1R',
    'HLT_Photon17_SC17HE_L1R_v1',
    'HLT_Photon20_Cleaned_L1R',
    'HLT_Photon20_NoHE_L1R',
    'HLT_Photon30_Cleaned_L1R',
    'HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1',
    'HLT_Photon35_Isol_Cleaned_L1R_v1',
    'HLT_Photon50_Cleaned_L1R_v1',
    'HLT_Photon50_NoHE_L1R',
    'HLT_Photon70_NoHE_Cleaned_L1R_v1',
    'HLT_PixelTracks_Multiplicity100',
    'HLT_PixelTracks_Multiplicity70',
    'HLT_PixelTracks_Multiplicity85',
    'HLT_QuadJet15U_v2',
    'HLT_QuadJet20U_v2',
    'HLT_QuadJet25U_v2',
    'HLT_RPCBarrelCosmics',
    'HLT_Random',
    'HLT_SingleIsoTau20_Trk15_MET20',
    'HLT_SingleIsoTau20_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_v2',
    'HLT_StoppedHSCP20_v3',
    'HLT_StoppedHSCP35_v3',
    'HLT_TechTrigHCALNoise',
    'HLT_TrackerCosmics',
    'HLT_ZeroBias',
    'HLT_ZeroBiasPixel_SingleTrack' ),
  OnlineHltMonitor = cms.vstring( 'AlCa_EcalEta',
    'AlCa_EcalPhiSym',
    'AlCa_EcalPi0',
    'AlCa_RPCMuonNoHits',
    'AlCa_RPCMuonNoTriggers',
    'AlCa_RPCMuonNormalisation',
    'HLT_Activity_CSC',
    'HLT_Activity_DT',
    'HLT_Activity_DT_Tuned',
    'HLT_Activity_Ecal_SC17',
    'HLT_Activity_Ecal_SC7',
    'HLT_BTagMu_DiJet10U_v1',
    'HLT_BTagMu_DiJet20U_Mu5_v1',
    'HLT_BTagMu_DiJet20U_v1',
    'HLT_DTErrors',
    'HLT_DiJetAve100U_v1',
    'HLT_DiJetAve15U',
    'HLT_DiJetAve30U',
    'HLT_DiJetAve50U',
    'HLT_DiJetAve70U_v2',
    'HLT_DoubleEle15_SW_L1R_v1',
    'HLT_DoubleEle4_SW_eeRes_L1R',
    'HLT_DoubleIsoTau15_OneLeg_Trk5',
    'HLT_DoubleIsoTau15_Trk5',
    'HLT_DoubleJet15U_ForwardBackward',
    'HLT_DoubleJet25U_ForwardBackward',
    'HLT_DoubleMu0_Quarkonium_LS_v1',
    'HLT_DoubleMu0_Quarkonium_v1',
    'HLT_DoubleMu3_v2',
    'HLT_DoubleMu5_v1',
    'HLT_DoublePhoton17_L1R',
    'HLT_DoublePhoton5_CEP_L1R',
    'HLT_EcalOnly_SumEt160_v2',
    'HLT_Ele10_MET45_v1',
    'HLT_Ele10_SW_L1R',
    'HLT_Ele12_SW_TightEleId_L1R',
    'HLT_Ele12_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele12_SW_TighterEleId_L1R_v1',
    'HLT_Ele17_SW_L1R',
    'HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1',
    'HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1',
    'HLT_Ele17_SW_TightEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TightEleId_L1R',
    'HLT_Ele17_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TighterEleId_L1R_v1',
    'HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_ExclDiJet30U_HFAND_v1',
    'HLT_ExclDiJet30U_HFOR_v1',
    'HLT_GlobalRunHPDNoise',
    'HLT_HT100U',
    'HLT_HT120U',
    'HLT_HT140U',
    'HLT_HT140U_Eta3_v1',
    'HLT_HT160U_v1',
    'HLT_HT200U_v1',
    'HLT_HT50U_v1',
    'HLT_HcalNZS',
    'HLT_HcalPhiSym',
    'HLT_IsoMu11_v1',
    'HLT_IsoMu9',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v2',
    'HLT_Jet100U_v2',
    'HLT_Jet140U_v1',
    'HLT_Jet15U',
    'HLT_Jet15U_HcalNoiseFiltered',
    'HLT_Jet30U',
    'HLT_Jet50U',
    'HLT_Jet70U_v2',
    'HLT_L1DoubleMuOpen',
    'HLT_L1ETT100',
    'HLT_L1ETT140_v1',
    'HLT_L1Jet10U',
    'HLT_L1Jet6U',
    'HLT_L1MET20',
    'HLT_L1Mu20',
    'HLT_L1Mu7_v1',
    'HLT_L1MuOpen',
    'HLT_L1MuOpen_AntiBPTX',
    'HLT_L1MuOpen_DT',
    'HLT_L1SingleEG2',
    'HLT_L1SingleEG8',
    'HLT_L1Tech_BSC_HighMultiplicity',
    'HLT_L1Tech_BSC_halo',
    'HLT_L1Tech_BSC_halo_forPhysicsBackground',
    'HLT_L1Tech_BSC_minBias',
    'HLT_L1Tech_BSC_minBias_OR',
    'HLT_L1Tech_HCAL_HF',
    'HLT_L1Tech_RPC_TTU_RBst1_collisions',
    'HLT_L1_BPTX',
    'HLT_L1_BPTX_MinusOnly',
    'HLT_L1_BPTX_PlusOnly',
    'HLT_L1_BptxXOR_BscMinBiasOR',
    'HLT_L2DoubleMu0',
    'HLT_L2DoubleMu20_NoVertex_v1',
    'HLT_L2Mu0_NoVertex',
    'HLT_L2Mu30_v1',
    'HLT_L2Mu7_v1',
    'HLT_LogMonitor',
    'HLT_MET100_v2',
    'HLT_MET45',
    'HLT_MET45_HT100U_v1',
    'HLT_MET45_HT120U_v1',
    'HLT_MET65',
    'HLT_MET80_v1',
    'HLT_MinBiasPixel_SingleTrack',
    'HLT_Mu0_TkMu0_OST_Jpsi',
    'HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1',
    'HLT_Mu11',
    'HLT_Mu13_v1',
    'HLT_Mu15_v1',
    'HLT_Mu20_NoVertex',
    'HLT_Mu3',
    'HLT_Mu3_TkMu0_OST_Jpsi',
    'HLT_Mu3_Track3_Jpsi',
    'HLT_Mu3_Track5_Jpsi_v1',
    'HLT_Mu5',
    'HLT_Mu5_Ele5_v1',
    'HLT_Mu5_Ele9_v1',
    'HLT_Mu5_HT50U_v1',
    'HLT_Mu5_HT70U_v1',
    'HLT_Mu5_Jet35U_v1',
    'HLT_Mu5_Jet50U_v2',
    'HLT_Mu5_L2Mu0',
    'HLT_Mu5_MET45_v1',
    'HLT_Mu5_Photon11_Cleaned_L1R_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi',
    'HLT_Mu5_Track0_Jpsi',
    'HLT_Mu7',
    'HLT_Mu9',
    'HLT_MultiVertex6',
    'HLT_MultiVertex8_L1ETT60',
    'HLT_Photon100_NoHE_Cleaned_L1R_v1',
    'HLT_Photon10_Cleaned_L1R',
    'HLT_Photon15_Cleaned_L1R',
    'HLT_Photon17_SC17HE_L1R_v1',
    'HLT_Photon20_Cleaned_L1R',
    'HLT_Photon20_NoHE_L1R',
    'HLT_Photon30_Cleaned_L1R',
    'HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1',
    'HLT_Photon35_Isol_Cleaned_L1R_v1',
    'HLT_Photon50_Cleaned_L1R_v1',
    'HLT_Photon50_NoHE_L1R',
    'HLT_Photon70_NoHE_Cleaned_L1R_v1',
    'HLT_PixelTracks_Multiplicity100',
    'HLT_PixelTracks_Multiplicity70',
    'HLT_PixelTracks_Multiplicity85',
    'HLT_QuadJet15U_v2',
    'HLT_QuadJet20U_v2',
    'HLT_QuadJet25U_v2',
    'HLT_RPCBarrelCosmics',
    'HLT_Random',
    'HLT_SingleIsoTau20_Trk15_MET20',
    'HLT_SingleIsoTau20_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_v2',
    'HLT_StoppedHSCP20_v3',
    'HLT_StoppedHSCP35_v3',
    'HLT_TechTrigHCALNoise',
    'HLT_TrackerCosmics',
    'HLT_ZeroBias',
    'HLT_ZeroBiasPixel_SingleTrack' ),
  OnlineHltResults = cms.vstring( 'HLTriggerFinalPath' ),
  OnlineMonitor = cms.vstring( 'DQM_FEDIntegrity',
    'HLT_Activity_CSC',
    'HLT_Activity_DT',
    'HLT_Activity_DT_Tuned',
    'HLT_Activity_Ecal_SC17',
    'HLT_Activity_Ecal_SC7',
    'HLT_BTagMu_DiJet10U_v1',
    'HLT_BTagMu_DiJet20U_Mu5_v1',
    'HLT_BTagMu_DiJet20U_v1',
    'HLT_Calibration',
    'HLT_DTErrors',
    'HLT_DiJetAve100U_v1',
    'HLT_DiJetAve15U',
    'HLT_DiJetAve30U',
    'HLT_DiJetAve50U',
    'HLT_DiJetAve70U_v2',
    'HLT_DoubleEle15_SW_L1R_v1',
    'HLT_DoubleEle4_SW_eeRes_L1R',
    'HLT_DoubleIsoTau15_OneLeg_Trk5',
    'HLT_DoubleIsoTau15_Trk5',
    'HLT_DoubleJet15U_ForwardBackward',
    'HLT_DoubleJet25U_ForwardBackward',
    'HLT_DoubleMu0_Quarkonium_LS_v1',
    'HLT_DoubleMu0_Quarkonium_v1',
    'HLT_DoubleMu3_v2',
    'HLT_DoubleMu5_v1',
    'HLT_DoublePhoton17_L1R',
    'HLT_DoublePhoton5_CEP_L1R',
    'HLT_EcalCalibration',
    'HLT_EcalOnly_SumEt160_v2',
    'HLT_Ele10_MET45_v1',
    'HLT_Ele10_SW_L1R',
    'HLT_Ele12_SW_TightEleId_L1R',
    'HLT_Ele12_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele12_SW_TighterEleId_L1R_v1',
    'HLT_Ele17_SW_L1R',
    'HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1',
    'HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1',
    'HLT_Ele17_SW_TightEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TightEleId_L1R',
    'HLT_Ele17_SW_TighterEleIdIsol_L1R_v1',
    'HLT_Ele17_SW_TighterEleId_L1R_v1',
    'HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1',
    'HLT_ExclDiJet30U_HFAND_v1',
    'HLT_ExclDiJet30U_HFOR_v1',
    'HLT_GlobalRunHPDNoise',
    'HLT_HT100U',
    'HLT_HT120U',
    'HLT_HT140U',
    'HLT_HT140U_Eta3_v1',
    'HLT_HT160U_v1',
    'HLT_HT200U_v1',
    'HLT_HT50U_v1',
    'HLT_HcalCalibration',
    'HLT_HcalNZS',
    'HLT_HcalPhiSym',
    'HLT_IsoMu11_v1',
    'HLT_IsoMu9',
    'HLT_IsoTrackHB_v2',
    'HLT_IsoTrackHE_v2',
    'HLT_Jet100U_v2',
    'HLT_Jet140U_v1',
    'HLT_Jet15U',
    'HLT_Jet15U_HcalNoiseFiltered',
    'HLT_Jet30U',
    'HLT_Jet50U',
    'HLT_Jet70U_v2',
    'HLT_L1DoubleMuOpen',
    'HLT_L1ETT100',
    'HLT_L1ETT140_v1',
    'HLT_L1Jet10U',
    'HLT_L1Jet6U',
    'HLT_L1MET20',
    'HLT_L1Mu20',
    'HLT_L1Mu7_v1',
    'HLT_L1MuOpen',
    'HLT_L1MuOpen_AntiBPTX',
    'HLT_L1MuOpen_DT',
    'HLT_L1SingleEG2',
    'HLT_L1SingleEG8',
    'HLT_L1Tech_BSC_HighMultiplicity',
    'HLT_L1Tech_BSC_halo',
    'HLT_L1Tech_BSC_halo_forPhysicsBackground',
    'HLT_L1Tech_BSC_minBias',
    'HLT_L1Tech_BSC_minBias_OR',
    'HLT_L1Tech_HCAL_HF',
    'HLT_L1Tech_RPC_TTU_RBst1_collisions',
    'HLT_L1_BPTX',
    'HLT_L1_BPTX_MinusOnly',
    'HLT_L1_BPTX_PlusOnly',
    'HLT_L1_BptxXOR_BscMinBiasOR',
    'HLT_L2DoubleMu0',
    'HLT_L2DoubleMu20_NoVertex_v1',
    'HLT_L2Mu0_NoVertex',
    'HLT_L2Mu30_v1',
    'HLT_L2Mu7_v1',
    'HLT_LogMonitor',
    'HLT_MET100_v2',
    'HLT_MET45',
    'HLT_MET45_HT100U_v1',
    'HLT_MET45_HT120U_v1',
    'HLT_MET65',
    'HLT_MET80_v1',
    'HLT_MinBiasPixel_SingleTrack',
    'HLT_Mu0_TkMu0_OST_Jpsi',
    'HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1',
    'HLT_Mu11',
    'HLT_Mu13_v1',
    'HLT_Mu15_v1',
    'HLT_Mu20_NoVertex',
    'HLT_Mu3',
    'HLT_Mu3_TkMu0_OST_Jpsi',
    'HLT_Mu3_Track3_Jpsi',
    'HLT_Mu3_Track5_Jpsi_v1',
    'HLT_Mu5',
    'HLT_Mu5_Ele5_v1',
    'HLT_Mu5_Ele9_v1',
    'HLT_Mu5_HT50U_v1',
    'HLT_Mu5_HT70U_v1',
    'HLT_Mu5_Jet35U_v1',
    'HLT_Mu5_Jet50U_v2',
    'HLT_Mu5_L2Mu0',
    'HLT_Mu5_MET45_v1',
    'HLT_Mu5_Photon11_Cleaned_L1R_v1',
    'HLT_Mu5_TkMu0_OST_Jpsi',
    'HLT_Mu5_Track0_Jpsi',
    'HLT_Mu7',
    'HLT_Mu9',
    'HLT_MultiVertex6',
    'HLT_MultiVertex8_L1ETT60',
    'HLT_Photon100_NoHE_Cleaned_L1R_v1',
    'HLT_Photon10_Cleaned_L1R',
    'HLT_Photon15_Cleaned_L1R',
    'HLT_Photon17_SC17HE_L1R_v1',
    'HLT_Photon20_Cleaned_L1R',
    'HLT_Photon20_NoHE_L1R',
    'HLT_Photon30_Cleaned_L1R',
    'HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1',
    'HLT_Photon35_Isol_Cleaned_L1R_v1',
    'HLT_Photon50_Cleaned_L1R_v1',
    'HLT_Photon50_NoHE_L1R',
    'HLT_Photon70_NoHE_Cleaned_L1R_v1',
    'HLT_PixelTracks_Multiplicity100',
    'HLT_PixelTracks_Multiplicity70',
    'HLT_PixelTracks_Multiplicity85',
    'HLT_QuadJet15U_v2',
    'HLT_QuadJet20U_v2',
    'HLT_QuadJet25U_v2',
    'HLT_RPCBarrelCosmics',
    'HLT_Random',
    'HLT_SingleIsoTau20_Trk15_MET20',
    'HLT_SingleIsoTau20_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_MET20',
    'HLT_SingleIsoTau30_Trk5_v2',
    'HLT_StoppedHSCP20_v3',
    'HLT_StoppedHSCP35_v3',
    'HLT_TechTrigHCALNoise',
    'HLT_TrackerCosmics',
    'HLT_ZeroBias',
    'HLT_ZeroBiasPixel_SingleTrack' ),
  Photon = cms.vstring( 'HLT_DoublePhoton17_L1R',
    'HLT_DoublePhoton5_CEP_L1R',
    'HLT_Photon100_NoHE_Cleaned_L1R_v1',
    'HLT_Photon17_SC17HE_L1R_v1',
    'HLT_Photon20_Cleaned_L1R',
    'HLT_Photon30_Cleaned_L1R',
    'HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1',
    'HLT_Photon35_Isol_Cleaned_L1R_v1',
    'HLT_Photon50_Cleaned_L1R_v1',
    'HLT_Photon70_NoHE_Cleaned_L1R_v1' ),
  RPCMonitor = cms.vstring( 'AlCa_RPCMuonNoHits',
    'AlCa_RPCMuonNoTriggers',
    'AlCa_RPCMuonNormalisation' ),
  TestEnables = cms.vstring( 'HLT_Calibration',
    'HLT_HcalCalibration' )
)

process.source = cms.Source( "DaqSource",
  evtsPerLS = cms.untracked.uint32( 0 ),
  processingMode = cms.untracked.string( "defaultMode" ),
  readerPluginName = cms.untracked.string( "FUShmReader" ),
  readerPset = cms.untracked.PSet(

  )
)

process.BTagRecord = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "JetTagComputerRecord" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.GlobalTag = cms.ESSource( "PoolDBESSource",
  appendToDataLabel = cms.string( "" ),
  timetype = cms.string( "runnumber" ),
  authenticationMethod = cms.untracked.uint32( 0 ),
  siteLocalConfig = cms.untracked.bool( False ),
  messagelevel = cms.untracked.uint32( 0 ),
  connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_COND_31X_GLOBALTAG" ),
  label = cms.untracked.string( "" ),
  DumpStat = cms.untracked.bool( False ),
  BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" ),
  globaltag = cms.string( "GR10_H_V9::All" ),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string( "." ),
    connectionRetrialPeriod = cms.untracked.int32( 10 ),
    idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
    messageLevel = cms.untracked.int32( 0 ),
    enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
    enableConnectionSharing = cms.untracked.bool( True ),
    enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
    connectionTimeOut = cms.untracked.int32( 0 ),
    connectionRetrialTimeOut = cms.untracked.int32( 60 )
  ),
  toGet = cms.VPSet(

  ),
  RefreshEachRun = cms.untracked.bool( True )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
  pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" ),
  appendToDataLabel = cms.string( "" )
)
process.L2RelativeCorrectionService = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2Relative" ),
  algorithm = cms.string( "IC5Calo" ),
  section = cms.string( "" ),
  era = cms.string( "Summer09_7TeV_ReReco332" )
)
process.L3AbsoluteCorrectionService = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L3Absolute" ),
  algorithm = cms.string( "IC5Calo" ),
  section = cms.string( "" ),
  era = cms.string( "Summer09_7TeV_ReReco332" )
)
process.MCJetCorrectorIcone5 = cms.ESSource( "JetCorrectionServiceChain",
  appendToDataLabel = cms.string( "" ),
  correctors = cms.vstring( "L2RelativeCorrectionService", "L3AbsoluteCorrectionService" ),
  label = cms.string( "MCJetCorrectorIcone5" )
)
process.MCJetCorrectorIcone5HF07 = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2Relative" ),
  algorithm = cms.string( "" ),
  section = cms.string( "" ),
  era = cms.string( "HLT" )
)
process.MCJetCorrectorIcone5Unit = cms.ESSource( "LXXXCorrectionService",
  appendToDataLabel = cms.string( "" ),
  level = cms.string( "L2RelativeFlat" ),
  algorithm = cms.string( "" ),
  section = cms.string( "" ),
  era = cms.string( "HLT" )
)
process.eegeom = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "EcalMappingRcd" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
  H2Mode = cms.untracked.bool( False ),
  toGet = cms.untracked.vstring( "GainWidths" ),
  appendToDataLabel = cms.string( "" )
)
process.essourceSev = cms.ESSource( "EmptyESSource",
  recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
  iovIsRunNotTime = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  firstValid = cms.vuint32( 1 )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
  rootNodeName = cms.string( "cmsMagneticField:MAGF" ),
  userControlledNamespace = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  geomXMLFiles = cms.vstring( "Geometry/CMSCommonData/data/normal/cmsextent.xml", "Geometry/CMSCommonData/data/cms.xml", "Geometry/CMSCommonData/data/cmsMagneticField.xml", "MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml", "MagneticField/GeomBuilder/data/MagneticFieldParameters_07_2pi.xml" )
)

process.hltHIPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltHIPixelLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.hltHIPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltHIPixelLayerTriplets" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3", "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltHISiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.AnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" ),
  MaxDPhi = cms.double( 1.6 ),
  appendToDataLabel = cms.string( "" )
)
process.AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  valueOverride = cms.int32( -1 ),
  appendToDataLabel = cms.string( "" ),
  nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
  mapLabels = cms.untracked.vstring( "090322_3_8t", "0t", "071212_2t", "071212_3t", "071212_3_5t", "090322_3_8t", "071212_4t" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  useRealWireGeometry = cms.bool( True ),
  useOnlyWiresInME1a = cms.bool( False ),
  useGangedStripsInME1a = cms.bool( True ),
  useCentreTIOffsets = cms.bool( False ),
  debugV = cms.untracked.bool( False ),
  useDDD = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  appendToDataLabel = cms.string( "" ),
  SelectedCalos = cms.vstring( "HCAL", "ZDC", "EcalBarrel", "EcalEndcap", "EcalPreshower", "TOWER" )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder",
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" ),
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.Chi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "Chi2EstimatorForRefit" ),
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.Chi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  ComponentName = cms.string( "Chi2" ),
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.DummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "DummyDetLayerGeometry" ),
  appendToDataLabel = cms.string( "" )
)
process.ESUnpackerWorkerESProducer = cms.ESProducer( "ESUnpackerWorkerESProducer",
  ComponentName = cms.string( "esRawToRecHit" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
  ),
  RHAlgo = cms.PSet(
    Type = cms.string( "ESRecHitWorker" ),
    ESGain = cms.int32( 2 ),
    ESMIPkeV = cms.double( 81.08 ),
    ESMIPADC = cms.double( 55.0 ),
    ESBaseline = cms.int32( 0 ),
    ESRecoAlgo = cms.int32( 0 )
  )
)
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder",
  appendToDataLabel = cms.string( "" )
)
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService",
  appendToDataLabel = cms.string( "" )
)
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True )
)
process.EcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  appendToDataLabel = cms.string( "" ),
  esMapping = cms.PSet(
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
  )
)
process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" ),
  appendToDataLabel = cms.string( "" )
)
process.EcalUnpackerWorkerESProducer = cms.ESProducer( "EcalUnpackerWorkerESProducer",
  ComponentName = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  DCCDataUnpacker = cms.PSet(
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    tccUnpacking = cms.bool( True ),
    srpUnpacking = cms.bool( False ),
    syncCheck = cms.bool( False ),
    feIdCheck = cms.bool( True ),
    headerUnpacking = cms.bool( False ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    feUnpacking = cms.bool( True ),
    forceKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( False )
  ),
  ElectronicsMapper = cms.PSet(
    numbXtalTSamples = cms.uint32( 10 ),
    numbTriggerTSamples = cms.uint32( 1 )
  ),
  UncalibRHAlgo = cms.PSet(
    Type = cms.string( "EcalUncalibRecHitWorkerWeights" )
  ),
  CalibRHAlgo = cms.PSet(
    flagsMapDBReco = cms.vint32( 0, 0, 0, 0, 4, -1, -1, -1, 4, 4, 6, 6, 6, 7, 8 ),
    Type = cms.string( "EcalRecHitWorkerSimple" ),
    killDeadChannels = cms.bool( True ),
    ChannelStatusToBeExcluded = cms.vint32( 10, 11, 12, 13, 14, 78, 142 ),
    laserCorrection = cms.bool( False )
  )
)
process.FastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "FastSteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.FastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "FastSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( True ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.FitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "FitterRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.FittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "FittingSmootherRK" ),
  Fitter = cms.string( "FitterRK" ),
  Smoother = cms.string( "SmootherRK" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.GlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.HITTRHBuilderWithoutRefit = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "HITTRHBuilderWithoutRefit" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "Fake" ),
  Matcher = cms.string( "Fake" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  Exclude = cms.untracked.string( "" ),
  H2Mode = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.KFFitterForRefitInsideOut = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "KFFitterForRefitInsideOut" ),
  Propagator = cms.string( "SmartPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2EstimatorForRefit" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFFitterSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "KFFitterSmootherForL2Muon" ),
  Fitter = cms.string( "KFTrajectoryFitterForL2Muon" ),
  Smoother = cms.string( "KFTrajectorySmootherForL2Muon" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.KFSmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFSmootherForMuonTrackLoader" ),
  Propagator = cms.string( "SmartPropagatorAnyOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFSmootherForRefitInsideOut = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFSmootherForRefitInsideOut" ),
  Propagator = cms.string( "SmartPropagatorAnyOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2EstimatorForRefit" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "KFTrajectoryFitterForL2Muon" ),
  Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "KFTrajectorySmootherForL2Muon" ),
  Propagator = cms.string( "FastSteppingHelixPropagatorOpposite" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.KFUpdatorESProducer = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "KFUpdator" ),
  appendToDataLabel = cms.string( "" )
)
process.L1GtTriggerMaskAlgoTrigTrivialProducer = cms.ESProducer( "L1GtTriggerMaskAlgoTrigTrivialProducer",
  appendToDataLabel = cms.string( "" ),
  TriggerMask = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )
)
process.L1GtTriggerMaskTechTrigTrivialProducer = cms.ESProducer( "L1GtTriggerMaskTechTrigTrivialProducer",
  appendToDataLabel = cms.string( "" ),
  TriggerMask = cms.vuint32( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 )
)
process.L3MuKFFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "L3MuKFFitter" ),
  Propagator = cms.string( "SmartPropagatorAny" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.hltMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  ComponentName = cms.string( "hltMeasurementTracker" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  HitMatcher = cms.string( "StandardMatcher" ),
  Regional = cms.bool( True ),
  OnDemand = cms.bool( True ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripModuleQualityDB = cms.bool( True ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  MaskBadAPVFibers = cms.bool( True ),
  UseStripStripQualityDB = cms.bool( True ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  SiStripQualityLabel = cms.string( "" ),
  switchOffPixelsIfEmpty = cms.bool( True ),
  pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
  stripClusterProducer = cms.string( "hltSiStripClusters" ),
  stripLazyGetterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
  appendToDataLabel = cms.string( "" ),
  inactivePixelDetectorLabels = cms.VInputTag(  ),
  inactiveStripDetectorLabels = cms.VInputTag(  ),
  badStripCuts = cms.PSet(
    TIB = cms.PSet(
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TOB = cms.PSet(
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet(
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet(
      maxBad = cms.uint32( 9999 ),
      maxConsecutiveBad = cms.uint32( 9999 )
    )
  )
)
process.MuonCkfTrajectoryBuilder = cms.ESProducer( "MuonCkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "muonCkfTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "muonCkfTrajectoryFilter" ),
  useSeedLayer = cms.bool( False ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  deltaEta = cms.double( 0.1 ),
  deltaPhi = cms.double( 0.1 ),
  appendToDataLabel = cms.string( "" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( False ),
  alwaysUseInvalidHits = cms.bool( True )
)
process.MuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer",
  appendToDataLabel = cms.string( "" )
)
process.MuonNumberingInitialization = cms.ESProducer( "MuonNumberingInitialization",
  appendToDataLabel = cms.string( "" )
)
process.MuonTransientTrackingRecHitBuilderESProducer = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "MuonRecHitBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.PixelCPEGenericESProducer = cms.ESProducer( "PixelCPEGenericESProducer",
  ComponentName = cms.string( "PixelCPEGeneric" ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  size_cutX = cms.double( 3.0 ),
  size_cutY = cms.double( 3.0 ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  inflate_errors = cms.bool( False ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  IrradiationBiasCorrection = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  TanLorentzAnglePerTesla = cms.double( 0.106 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  compatibiltyWith11 = cms.untracked.bool( True ),
  useDDD = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.RungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  ComponentName = cms.string( "RungeKuttaTrackerPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Mass = cms.double( 0.105 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True ),
  ptMin = cms.double( -1.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  AutomaticNormalization = cms.bool( False ),
  NormalizationFactor = cms.double( 1.0 ),
  printDebug = cms.untracked.bool( False ),
  APVGain = cms.VPSet(
    cms.PSet(
      Record = cms.string( "SiStripApvGainRcd" ),
      Label = cms.untracked.string( "" ),
      NormalizationFactor = cms.untracked.double( 1.0 )
    ),
    cms.PSet(
      Record = cms.string( "SiStripApvGain2Rcd" ),
      Label = cms.untracked.string( "" ),
      NormalizationFactor = cms.untracked.double( 1.0 )
    )
  )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet(
    cms.PSet(
      record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(
      record = cms.string( "RunInfoRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
  ZFieldInTesla = cms.double( 0.0 ),
  label = cms.untracked.string( "slave_0" ),
  appendToDataLabel = cms.string( "" )
)
process.SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_20" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "2_0T" )
  )
)
process.SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_30" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_0T" )
  )
)
process.SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_35" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_5T" )
  )
)
process.SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_38" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "3_8T" )
  )
)
process.SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  label = cms.untracked.string( "slave_40" ),
  version = cms.string( "OAE_1103l_071212" ),
  appendToDataLabel = cms.string( "" ),
  parameters = cms.PSet(
    BValue = cms.string( "4_0T" )
  )
)
process.SmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAlong" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorAnyOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  appendToDataLabel = cms.string( "" )
)
process.SmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  ComponentName = cms.string( "SmartPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorOpposite" ),
  appendToDataLabel = cms.string( "" )
)
process.SmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "SmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "anyDirection" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.SteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  ComponentName = cms.string( "SteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useInTeslaFromMagField = cms.bool( False ),
  SetVBFPointer = cms.bool( False ),
  useMagVolumes = cms.bool( True ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  ApplyRadX0Correction = cms.bool( True ),
  AssumeNoMaterial = cms.bool( False ),
  NoErrorPropagation = cms.bool( False ),
  debug = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  returnTangentPlane = cms.bool( True ),
  sendLogWarning = cms.bool( False ),
  useTuningForL2Speed = cms.bool( False ),
  useEndcapShiftsInZ = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  appendToDataLabel = cms.string( "" )
)
process.StraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "StraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  appendToDataLabel = cms.string( "" )
)
process.StripCPEfromTrackAngleESProducer = cms.ESProducer( "StripCPEESProducer",
  ComponentName = cms.string( "StripCPEfromTrackAngle" ),
  appendToDataLabel = cms.string( "" ),
  TanDiffusionAngle = cms.double( 0.01 ),
  ThicknessRelativeUncertainty = cms.double( 0.02 ),
  NoiseThreshold = cms.double( 2.3 ),
  MaybeNoiseThreshold = cms.double( 3.5 ),
  UncertaintyScaling = cms.double( 1.42 ),
  MinimumUncertainty = cms.double( 0.01 )
)
process.TTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "TTRHBuilderPixelOnly" ),
  StripCPE = cms.string( "Fake" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  alignmentsLabel = cms.string( "" ),
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( True ),
  fromDDD = cms.bool( False )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  fromDDD = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.TrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  trackerGeometryLabel = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" ),
  appendToDataLabel = cms.string( "" )
)
process.VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "0t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_2t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_0" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_2t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_20" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_3t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_3t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_30" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_3_5t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_3_5t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_35" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "090322_3_8t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  overrideMasterSector = cms.bool( False ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_38" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  label = cms.untracked.string( "071212_4t" ),
  debugBuilder = cms.untracked.bool( False ),
  version = cms.string( "grid_1103l_071212_4t" ),
  overrideMasterSector = cms.bool( True ),
  useParametrizedTrackerField = cms.bool( True ),
  paramLabel = cms.string( "slave_40" ),
  appendToDataLabel = cms.string( "" ),
  scalingVolumes = cms.vint32(  ),
  scalingFactors = cms.vdouble(  ),
  findVolumeTolerance = cms.double( 0.0 ),
  cacheLastVolume = cms.untracked.bool( True ),
  timerOn = cms.untracked.bool( False )
)
process.XMLFromDBSource = cms.ESProducer( "XMLIdealGeometryESProducer",
  rootDDName = cms.string( "cms:OCMS" ),
  label = cms.string( "Extended" ),
  appendToDataLabel = cms.string( "" )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  appendToDataLabel = cms.string( "" ),
  applyAlignment = cms.bool( False )
)
process.bJetRegionalTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "bJetRegionalTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "bJetRegionalTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.bJetRegionalTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "bJetRegionalTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 1.0 )
  )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.ckfBaseTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "ckfBaseTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  SeverityLevels = cms.VPSet(
    cms.PSet(
      RecHitFlags = cms.vstring( "" ),
      ChannelStatus = cms.vstring( "" ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(
      Level = cms.int32( 1 ),
      RecHitFlags = cms.vstring( "" ),
      ChannelStatus = cms.vstring( "HcalCellCaloTowerProb" )
    ),
    cms.PSet(
      Level = cms.int32( 5 ),
      RecHitFlags = cms.vstring( "HSCP_R1R2", "HSCP_FracLeader", "HSCP_OuterEnergy", "HSCP_ExpFit", "ADCSaturationBit" ),
      ChannelStatus = cms.vstring( "" )
    ),
    cms.PSet(
      Level = cms.int32( 8 ),
      RecHitFlags = cms.vstring( "HBHEHpdHitMultiplicity", "HBHEPulseShape", "HOBit", "HFDigiTime", "HFInTimeWindow", "HFS8S1Ratio", "ZDCBit", "CalibrationBit", "TimingErrorBit" ),
      ChannelStatus = cms.vstring( "" )
    ),
    cms.PSet(
      Level = cms.int32( 11 ),
      RecHitFlags = cms.vstring( "HFLongShort" ),
      ChannelStatus = cms.vstring( "" )
    ),
    cms.PSet(
      Level = cms.int32( 12 ),
      RecHitFlags = cms.vstring( "" ),
      ChannelStatus = cms.vstring( "HcalCellCaloTowerMask" )
    ),
    cms.PSet(
      Level = cms.int32( 15 ),
      RecHitFlags = cms.vstring( "" ),
      ChannelStatus = cms.vstring( "HcalCellHot" )
    ),
    cms.PSet(
      Level = cms.int32( 20 ),
      RecHitFlags = cms.vstring( "" ),
      ChannelStatus = cms.vstring( "HcalCellOff", "HcalCellDead" )
    )
  ),
  DropChannelStatusBits = cms.vstring( "HcalCellMask", "HcalCellOff", "HcalCellDead" ),
  appendToDataLabel = cms.string( "" ),
  RecoveredRecHitBits = cms.vstring( "TimingAddedBit", "TimingSubtractedBit" )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer",
  file = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" ),
  dump = cms.untracked.vstring(  )
)
process.hltCkfTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltCkfTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "ckfBaseTrajectoryFilter" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( True ),
  appendToDataLabel = cms.string( "" )
)
process.hltCkfTrajectoryBuilderMumu = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltCkfTrajectoryBuilderMumu" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltCkfTrajectoryFilterMumu" ),
  maxCand = cms.int32( 3 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltCkfTrajectoryFilterMumu = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltCkfTrajectoryFilterMumu" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 5 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 3.0 )
  )
)
process.hltKFFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  ComponentName = cms.string( "hltKFFitter" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  ComponentName = cms.string( "hltKFFittingSmoother" ),
  Fitter = cms.string( "hltKFFitter" ),
  Smoother = cms.string( "hltKFSmoother" ),
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  MinNumberOfHits = cms.int32( 5 ),
  RejectTracks = cms.bool( True ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltKFSmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  ComponentName = cms.string( "hltKFSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  Updator = cms.string( "KFUpdator" ),
  Estimator = cms.string( "Chi2" ),
  RecoGeometry = cms.string( "DummyDetLayerGeometry" ),
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  appendToDataLabel = cms.string( "" )
)
process.hltMixedLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltMixedLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg", "FPix2_pos+TEC1_pos", "FPix2_pos+TEC2_pos", "TEC1_pos+TEC2_pos", "TEC2_pos+TEC3_pos", "FPix2_neg+TEC1_neg", "FPix2_neg+TEC2_neg", "TEC1_neg+TEC2_neg", "TEC2_neg+TEC3_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(
    useRingSlector = cms.bool( True ),
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    minRing = cms.int32( 1 ),
    maxRing = cms.int32( 1 )
  )
)
process.hltMuTrackJpsiTrajectoryBuilder = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "hltMuTrackJpsiTrajectoryBuilder" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "hltMuTrackJpsiTrajectoryFilter" ),
  maxCand = cms.int32( 1 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.hltMuTrackJpsiTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "hltMuTrackJpsiTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 8 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 1.0 )
  )
)
process.hltPixelLayerPairs = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltPixelLayerPairs" ),
  layerList = cms.vstring( "BPix1+BPix2", "BPix1+BPix3", "BPix2+BPix3", "BPix1+FPix1_pos", "BPix1+FPix1_neg", "BPix1+FPix2_pos", "BPix1+FPix2_neg", "BPix2+FPix1_pos", "BPix2+FPix1_neg", "BPix2+FPix2_pos", "BPix2+FPix2_neg", "FPix1_pos+FPix2_pos", "FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.hltPixelLayerTriplets = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "hltPixelLayerTriplets" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3", "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.muonCkfTrajectoryFilter = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "muonCkfTrajectoryFilter" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    chargeSignificance = cms.double( -1.0 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( -1 ),
    maxConsecLostHits = cms.int32( 1 ),
    minimumNumberOfHits = cms.int32( 5 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  appendToDataLabel = cms.string( "" )
)
process.pixellayertripletsHITHB = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "PixelLayerTripletsHITHB" ),
  layerList = cms.vstring( "BPix1+BPix2+BPix3" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.pixellayertripletsHITHE = cms.ESProducer( "SeedingLayersESProducer",
  appendToDataLabel = cms.string( "" ),
  ComponentName = cms.string( "PixelLayerTripletsHITHE" ),
  layerList = cms.vstring( "BPix1+BPix2+FPix1_pos", "BPix1+BPix2+FPix1_neg", "BPix1+FPix1_pos+FPix2_pos", "BPix1+FPix1_neg+FPix2_neg" ),
  BPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0027 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.006 )
  ),
  FPix = cms.PSet(
    useErrorsFromParam = cms.bool( True ),
    hitErrorRPhi = cms.double( 0.0051 ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    HitProducer = cms.string( "hltSiPixelRecHits" ),
    hitErrorRZ = cms.double( 0.0036 )
  ),
  TEC = cms.PSet(

  )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  appendToDataLabel = cms.string( "" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer",
  appendToDataLabel = cms.string( "" )
)
process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.softLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  appendToDataLabel = cms.string( "" ),
  distance = cms.double( 0.5 )
)
process.softLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  appendToDataLabel = cms.string( "" ),
  ipSign = cms.string( "any" )
)
process.trackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  appendToDataLabel = cms.string( "" ),
  nthTrack = cms.int32( 2 ),
  impactParameterType = cms.int32( 0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  trackQualityClass = cms.string( "any" )
)
process.trajBuilderL3 = cms.ESProducer( "CkfTrajectoryBuilderESProducer",
  ComponentName = cms.string( "trajBuilderL3" ),
  updator = cms.string( "KFUpdator" ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  estimator = cms.string( "Chi2" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltMeasurementTracker" ),
  trajectoryFilterName = cms.string( "trajFilterL3" ),
  maxCand = cms.int32( 5 ),
  lostHitPenalty = cms.double( 30.0 ),
  intermediateCleaning = cms.bool( True ),
  alwaysUseInvalidHits = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)
process.trajFilterL3 = cms.ESProducer( "TrajectoryFilterESProducer",
  ComponentName = cms.string( "trajFilterL3" ),
  appendToDataLabel = cms.string( "" ),
  filterPset = cms.PSet(
    minimumNumberOfHits = cms.int32( 5 ),
    minHitsMinPt = cms.int32( 3 ),
    ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
    maxLostHits = cms.int32( 1 ),
    maxNumberOfHits = cms.int32( 7 ),
    maxConsecLostHits = cms.int32( 1 ),
    chargeSignificance = cms.double( -1.0 ),
    nSigmaMinPt = cms.double( 5.0 ),
    minPt = cms.double( 0.9 )
  )
)
process.trajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "TrajectoryCleanerBySharedHits" ),
  appendToDataLabel = cms.string( "" ),
  fractionShared = cms.double( 0.5 ),
  allowSharedFirstHit = cms.bool( False )
)
process.ttrhbwr = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "WithTrackAngle" ),
  StripCPE = cms.string( "StripCPEfromTrackAngle" ),
  PixelCPE = cms.string( "PixelCPEGeneric" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  appendToDataLabel = cms.string( "" )
)

process.DQM = cms.Service( "DQM" )
process.DQMStore = cms.Service( "DQMStore",
  verbose = cms.untracked.int32( 0 ),
  verboseQT = cms.untracked.int32( 0 ),
  collateHistograms = cms.untracked.bool( False ),
  referenceFileName = cms.untracked.string( "" )
)
process.DTDataIntegrityTask = cms.Service( "DTDataIntegrityTask",
  getSCInfo = cms.untracked.bool( True ),
  processingMode = cms.untracked.string( "HLT" )
)
process.FUShmDQMOutputService = cms.Service( "FUShmDQMOutputService",
  initialMessageBufferSize = cms.untracked.int32( 1000000 ),
  lumiSectionsPerUpdate = cms.double( 1.0 ),
  useCompression = cms.bool( True ),
  compressionLevel = cms.int32( 1 ),
  lumiSectionInterval = cms.untracked.int32( 0 )
)
process.MessageLogger = cms.Service( "MessageLogger",
  destinations = cms.untracked.vstring( "warnings", "errors", "infos", "debugs", "cout", "cerr" ),
  categories = cms.untracked.vstring( "FwkJob", "FwkReport", "FwkSummary", "Root_NoDictionary" ),
  statistics = cms.untracked.vstring( "cerr" ),
  cerr = cms.untracked.PSet(
    INFO = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    noTimeStamps = cms.untracked.bool( False ),
    FwkReport = cms.untracked.PSet(
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 0 )
    ),
    default = cms.untracked.PSet(
      limit = cms.untracked.int32( 10000000 )
    ),
    Root_NoDictionary = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkJob = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkSummary = cms.untracked.PSet(
      reportEvery = cms.untracked.int32( 1 ),
      limit = cms.untracked.int32( 10000000 )
    ),
    threshold = cms.untracked.string( "INFO" ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  cout = cms.untracked.PSet(
    threshold = cms.untracked.string( "ERROR" ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  errors = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  warnings = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  infos = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    Root_NoDictionary = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    placeholder = cms.untracked.bool( True ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  debugs = cms.untracked.PSet(
    threshold = cms.untracked.string( "INFO" ),
    placeholder = cms.untracked.bool( True ),
    limit = cms.untracked.string( "" ),
    timespan = cms.untracked.string( "" ),
    suppressInfo = cms.untracked.vstring(  ),
    suppressWarning = cms.untracked.vstring(  ),
    suppressDebug = cms.untracked.vstring(  )
  ),
  default = cms.untracked.PSet(

  ),
  fwkJobReports = cms.untracked.vstring( "FrameworkJobReport" ),
  FrameworkJobReport = cms.untracked.PSet(
    default = cms.untracked.PSet(
      limit = cms.untracked.int32( 0 )
    ),
    FwkJob = cms.untracked.PSet(
      limit = cms.untracked.int32( 10000000 )
    )
  ),
  debugModules = cms.untracked.vstring(  ),
  suppressDebug = cms.untracked.vstring(  ),
  suppressInfo = cms.untracked.vstring(  ),
  suppressWarning = cms.untracked.vstring( "hltOnlineBeamSpot", "hltPixelTracksForMinBias", "hltPixelTracksForHighMult", "hltHITPixelTracksHE", "hltHITPixelTracksHB", "hltSiPixelClusters", "hltPixelTracks" ),
  threshold = cms.untracked.string( "INFO" ),
  limit = cms.untracked.string( "" ),
  timespan = cms.untracked.string( "" )
)
process.MicroStateService = cms.Service( "MicroStateService" )
process.ModuleWebRegistry = cms.Service( "ModuleWebRegistry" )
process.PrescaleService = cms.Service( "PrescaleService",
  lvl1DefaultLabel = cms.untracked.string( "3.2E30" ),
  lvl1Labels = cms.vstring( "1E32", "8E31", "6E31", "4E31", "2E31" ),
  prescaleTable = cms.VPSet(
    cms.PSet(
      pathName = cms.string( "HLT_Activity_CSC" ),
      prescales = cms.vuint32( 60, 60, 60, 60, 60 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Activity_DT" ),
      prescales = cms.vuint32( 4, 4, 4, 4, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Activity_Ecal_SC7" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Jet6U" ),
      prescales = cms.vuint32( 130, 130, 130, 130, 130 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Jet10U" ),
      prescales = cms.vuint32( 600, 600, 600, 600, 600 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet15U" ),
      prescales = cms.vuint32( 20, 20, 20, 20, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet15U_HcalNoiseFiltered" ),
      prescales = cms.vuint32( 20, 20, 20, 20, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet30U" ),
      prescales = cms.vuint32( 1000, 800, 600, 400, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet50U" ),
      prescales = cms.vuint32( 140, 100, 80, 60, 30 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Jet70U_v2" ),
      prescales = cms.vuint32( 25, 20, 15, 10, 5 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DiJetAve15U" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DiJetAve30U" ),
      prescales = cms.vuint32( 500, 400, 300, 200, 100 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DiJetAve50U" ),
      prescales = cms.vuint32( 65, 50, 40, 30, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DiJetAve70U_v2" ),
      prescales = cms.vuint32( 25, 20, 15, 10, 5 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DoubleJet15U_ForwardBackward" ),
      prescales = cms.vuint32( 16, 12, 8, 6, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DoubleJet25U_ForwardBackward" ),
      prescales = cms.vuint32( 8, 6, 4, 3, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_QuadJet15U_v2" ),
      prescales = cms.vuint32( 16, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1ETT100" ),
      prescales = cms.vuint32( 3000, 3000, 3000, 3000, 3000 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1ETT140_v1" ),
      prescales = cms.vuint32( 3000, 2400, 1800, 1200, 600 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1MET20" ),
      prescales = cms.vuint32( 1000, 800, 600, 400, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_MET45" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_MET65" ),
      prescales = cms.vuint32( 16, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_HT50U_v1" ),
      prescales = cms.vuint32( 50, 50, 50, 50, 50 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_HT100U" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_HT120U" ),
      prescales = cms.vuint32( 16, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1MuOpen" ),
      prescales = cms.vuint32( 7000, 5600, 4200, 2800, 1400 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1MuOpen_DT" ),
      prescales = cms.vuint32( 700, 560, 420, 280, 140 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1MuOpen_AntiBPTX" ),
      prescales = cms.vuint32( 30, 30, 30, 30, 30 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Mu7_v1" ),
      prescales = cms.vuint32( 1000, 800, 600, 400, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Mu20" ),
      prescales = cms.vuint32( 350, 280, 200, 140, 70 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L2Mu0_NoVertex" ),
      prescales = cms.vuint32( 6500, 5000, 4000, 3000, 2000 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L2Mu7_v1" ),
      prescales = cms.vuint32( 100, 80, 60, 40, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L2Mu30_v1" ),
      prescales = cms.vuint32( 16, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu3" ),
      prescales = cms.vuint32( 1000, 800, 600, 400, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu5" ),
      prescales = cms.vuint32( 350, 280, 200, 140, 70 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu7" ),
      prescales = cms.vuint32( 50, 40, 30, 20, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu9" ),
      prescales = cms.vuint32( 16, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1DoubleMuOpen" ),
      prescales = cms.vuint32( 650, 500, 400, 300, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L2DoubleMu0" ),
      prescales = cms.vuint32( 60, 48, 35, 24, 12 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DoubleMu0" ),
      prescales = cms.vuint32( 50, 40, 30, 20, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu5_L2Mu0" ),
      prescales = cms.vuint32( 25, 20, 15, 10, 5 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu3_Track3_Jpsi" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Mu5_Track0_Jpsi" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleEG2" ),
      prescales = cms.vuint32( 4000, 4000, 4000, 4000, 4000 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1SingleEG8" ),
      prescales = cms.vuint32( 25000, 20000, 15000, 10000, 5000 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Ele10_SW_L1R" ),
      prescales = cms.vuint32( 60, 60, 60, 60, 60 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Ele12_SW_TightEleId_L1R" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Ele12_SW_TighterEleId_L1R_v1" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Ele17_SW_L1R" ),
      prescales = cms.vuint32( 80, 65, 50, 35, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon10_Cleaned_L1R" ),
      prescales = cms.vuint32( 400, 400, 400, 400, 400 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon15_Cleaned_L1R" ),
      prescales = cms.vuint32( 2000, 1600, 1200, 800, 400 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon20_NoHE_L1R" ),
      prescales = cms.vuint32( 650, 500, 400, 300, 200 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon20_Cleaned_L1R" ),
      prescales = cms.vuint32( 125, 100, 70, 50, 25 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon30_Cleaned_L1R" ),
      prescales = cms.vuint32( 25, 20, 15, 10, 5 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Photon50_NoHE_L1R" ),
      prescales = cms.vuint32( 165, 130, 100, 70, 35 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_SingleIsoTau20_Trk5_MET20" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_SingleIsoTau30_Trk5_v2" ),
      prescales = cms.vuint32( 40, 32, 25, 16, 8 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_DoubleIsoTau15_OneLeg_Trk5" ),
      prescales = cms.vuint32( 14, 10, 8, 6, 3 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_BTagMu_DiJet10U_v1" ),
      prescales = cms.vuint32( 17, 13, 10, 7, 4 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_ZeroBias" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_ZeroBiasPixel_SingleTrack" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_MinBiasPixel_SingleTrack" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_MultiVertex6" ),
      prescales = cms.vuint32( 40, 40, 40, 40, 40 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_MultiVertex8_L1ETT60" ),
      prescales = cms.vuint32( 40, 40, 40, 40, 40 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1_BptxXOR_BscMinBiasOR" ),
      prescales = cms.vuint32( 20, 20, 20, 20, 20 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_minBias_OR" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_minBias" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_halo" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_halo_forPhysicsBackground" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_BSC_HighMultiplicity" ),
      prescales = cms.vuint32( 500, 400, 300, 200, 100 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_RPC_TTU_RBst1_collisions" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1Tech_HCAL_HF" ),
      prescales = cms.vuint32( 4, 3, 2, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_RPCBarrelCosmics" ),
      prescales = cms.vuint32( 100, 100, 100, 100, 100 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_HcalPhiSym" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_PixelTracks_Multiplicity70" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_GlobalRunHPDNoise" ),
      prescales = cms.vuint32( 80, 80, 80, 80, 80 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1_BPTX" ),
      prescales = cms.vuint32( 35, 28, 20, 14, 7 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1_BPTX_MinusOnly" ),
      prescales = cms.vuint32( 5, 4, 3, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_L1_BPTX_PlusOnly" ),
      prescales = cms.vuint32( 5, 4, 3, 2, 1 )
    ),
    cms.PSet(
      pathName = cms.string( "HLT_Random" ),
      prescales = cms.vuint32( 600, 600, 600, 600, 600 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_EcalPhiSym" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_EcalPi0" ),
      prescales = cms.vuint32( 3, 3, 3, 3, 3 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_EcalEta" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_RPCMuonNoHits" ),
      prescales = cms.vuint32( 7, 5, 4, 3, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_RPCMuonNoTriggers" ),
      prescales = cms.vuint32( 7, 5, 4, 3, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "AlCa_RPCMuonNormalisation" ),
      prescales = cms.vuint32( 7, 5, 4, 3, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "DQM_FEDIntegrity" ),
      prescales = cms.vuint32( 2, 2, 2, 2, 2 )
    ),
    cms.PSet(
      pathName = cms.string( "HLTMONOutput" ),
      prescales = cms.vuint32( 40, 40, 40, 40, 40 )
    ),
    cms.PSet(
      pathName = cms.string( "NanoDSTOutput" ),
      prescales = cms.vuint32( 10, 10, 10, 10, 10 )
    )
  )
)
process.UpdaterService = cms.Service( "UpdaterService" )

process.hlt1EcalOnlySumET160 = cms.HLTFilter( "HLTGlobalSumsCaloMET",
  inputTag = cms.InputTag( "hltEcalOnlyMet" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 160.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1HighMult100 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
  MinPt = cms.double( 0.2 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.0 ),
  MaxVz = cms.double( 10.0 ),
  MinTrks = cms.int32( 100 ),
  MinSep = cms.double( 0.12 )
)
process.hlt1HighMult70 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
  MinPt = cms.double( 0.2 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.0 ),
  MaxVz = cms.double( 10.0 ),
  MinTrks = cms.int32( 70 ),
  MinSep = cms.double( 0.12 )
)
process.hlt1HighMult85 = cms.HLTFilter( "HLTSingleVertexPixelTrackFilter",
  vertexCollection = cms.InputTag( "hltPixelVerticesForHighMult" ),
  trackCollection = cms.InputTag( "hltPixelCandsForHighMult" ),
  MinPt = cms.double( 0.2 ),
  MaxPt = cms.double( 10000.0 ),
  MaxEta = cms.double( 2.0 ),
  MaxVz = cms.double( 10.0 ),
  MinTrks = cms.int32( 85 ),
  MinSep = cms.double( 0.12 )
)
process.hlt1MET100 = cms.HLTFilter( "HLT1CaloMET",
  inputTag = cms.InputTag( "hltMet" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 100.0 ),
  MaxEta = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1MET45 = cms.HLTFilter( "HLT1CaloMET",
  inputTag = cms.InputTag( "hltMet" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 45.0 ),
  MaxEta = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1MET65 = cms.HLTFilter( "HLT1CaloMET",
  inputTag = cms.InputTag( "hltMet" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 65.0 ),
  MaxEta = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1MET80 = cms.HLTFilter( "HLT1CaloMET",
  inputTag = cms.InputTag( "hltMet" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 80.0 ),
  MaxEta = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet100U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 100.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet140U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 140.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet15U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet30U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet35U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 35.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet50U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 50.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt1jet70U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 70.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hlt4jet15U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 4 )
)
process.hlt4jet20U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 4 )
)
process.hlt4jet25U = cms.HLTFilter( "HLT1CaloJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 25.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 4 )
)
process.hltActivityPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.14 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( False )
)
process.hltActivityR9Shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltActivityR9shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltActivityStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.15 ),
    OrderedHitsFactoryPSet = cms.PSet(
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 3.0 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    measurementTrackerName = cms.string( "hltMeasurementTracker" ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.2 ),
    PhiMax2 = cms.double( 0.004 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.15 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.09 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.09 ),
    hbheInstance = cms.string( "" ),
    rMinI = cms.double( -0.2 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 )
  )
)
process.hltAlCaEtaRecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
  barrelHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  barrelClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersBarrel" ),
  endcapHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  endcapClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersEndcap" ),
  doSelBarrel = cms.bool( True ),
  doSelEndcap = cms.bool( True ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  preshRecHitProducer = cms.InputTag( "hltESRegionalPi0EtaRecHit:EcalRecHitsES" ),
  storeRecHitES = cms.bool( True ),
  debugLevel = cms.int32( 0 ),
  barrelSelection = cms.PSet(
    selePtGamma = cms.double( 1.2 ),
    selePtPair = cms.double( 4.0 ),
    seleS4S9Gamma = cms.double( 0.87 ),
    seleS9S25Gamma = cms.double( 0.8 ),
    seleMinvMaxBarrel = cms.double( 0.8 ),
    seleMinvMinBarrel = cms.double( 0.3 ),
    ptMinForIsolation = cms.double( 0.5 ),
    removePi0CandidatesForEta = cms.bool( True ),
    massLowPi0Cand = cms.double( 0.084 ),
    massHighPi0Cand = cms.double( 0.156 ),
    seleIso = cms.double( 0.5 ),
    seleBeltDR = cms.double( 0.3 ),
    seleBeltDeta = cms.double( 0.1 ),
    store5x5RecHitEB = cms.bool( True ),
    barrelHitCollection = cms.string( "etaEcalRecHitsEB" )
  ),
  endcapSelection = cms.PSet(
    seleMinvMaxEndCap = cms.double( 0.9 ),
    seleMinvMinEndCap = cms.double( 0.2 ),
    region1_EndCap = cms.double( 2.0 ),
    selePtGammaEndCap_region1 = cms.double( 1.0 ),
    selePtPairEndCap_region1 = cms.double( 3.0 ),
    region2_EndCap = cms.double( 2.5 ),
    selePtGammaEndCap_region2 = cms.double( 1.0 ),
    selePtPairEndCap_region2 = cms.double( 3.0 ),
    selePtGammaEndCap_region3 = cms.double( 0.7 ),
    selePtPairEndCap_region3 = cms.double( 3.0 ),
    seleS4S9GammaEndCap = cms.double( 0.9 ),
    seleS9S25GammaEndCap = cms.double( 0.85 ),
    ptMinForIsolationEndCap = cms.double( 0.5 ),
    seleBeltDREndCap = cms.double( 0.3 ),
    seleBeltDetaEndCap = cms.double( 0.1 ),
    seleIsoEndCap = cms.double( 0.5 ),
    store5x5RecHitEE = cms.bool( True ),
    endcapHitCollection = cms.string( "etaEcalRecHitsEE" ),
    selePtPairMaxEndCap_region3 = cms.double( 9999.0 )
  ),
  preshowerSelection = cms.PSet(
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshCalibPlaneX = cms.double( 1.0 ),
    preshCalibPlaneY = cms.double( 0.7 ),
    preshCalibGamma = cms.double( 0.024 ),
    preshCalibMIP = cms.double( 9.0e-05 ),
    debugLevelES = cms.string( "" ),
    ESCollection = cms.string( "etaEcalRecHitsES" )
  )
)
process.hltAlCaPhiSymStream = cms.HLTFilter( "HLTEcalPhiSymFilter",
  barrelHitCollection = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  endcapHitCollection = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  phiSymBarrelHitCollection = cms.string( "phiSymEcalRecHitsEB" ),
  phiSymEndcapHitCollection = cms.string( "phiSymEcalRecHitsEE" ),
  eCut_barrel = cms.double( 0.15 ),
  eCut_endcap = cms.double( 0.75 ),
  eCut_barrel_high = cms.double( 999999.0 ),
  eCut_endcap_high = cms.double( 999999.0 ),
  statusThreshold = cms.uint32( 3 ),
  useRecoFlag = cms.bool( False )
)
process.hltAlCaPi0RecHitsFilter = cms.HLTFilter( "HLTEcalResonanceFilter",
  barrelHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  barrelClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersBarrel" ),
  endcapHits = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  endcapClusters = cms.InputTag( "hltSimple3x3Clusters:Simple3x3ClustersEndcap" ),
  doSelBarrel = cms.bool( True ),
  doSelEndcap = cms.bool( True ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  preshRecHitProducer = cms.InputTag( "hltESRegionalPi0EtaRecHit:EcalRecHitsES" ),
  storeRecHitES = cms.bool( True ),
  debugLevel = cms.int32( 0 ),
  barrelSelection = cms.PSet(
    selePtGamma = cms.double( 1.3 ),
    selePtPair = cms.double( 2.6 ),
    seleS4S9Gamma = cms.double( 0.83 ),
    seleS9S25Gamma = cms.double( 0.0 ),
    seleMinvMaxBarrel = cms.double( 0.23 ),
    seleMinvMinBarrel = cms.double( 0.04 ),
    ptMinForIsolation = cms.double( 0.5 ),
    removePi0CandidatesForEta = cms.bool( False ),
    massLowPi0Cand = cms.double( 0.084 ),
    massHighPi0Cand = cms.double( 0.156 ),
    seleIso = cms.double( 0.5 ),
    seleBeltDR = cms.double( 0.2 ),
    seleBeltDeta = cms.double( 0.05 ),
    store5x5RecHitEB = cms.bool( False ),
    barrelHitCollection = cms.string( "pi0EcalRecHitsEB" )
  ),
  endcapSelection = cms.PSet(
    seleMinvMaxEndCap = cms.double( 0.3 ),
    seleMinvMinEndCap = cms.double( 0.05 ),
    region1_EndCap = cms.double( 2.0 ),
    selePtGammaEndCap_region1 = cms.double( 0.6 ),
    selePtPairEndCap_region1 = cms.double( 2.5 ),
    region2_EndCap = cms.double( 2.5 ),
    selePtGammaEndCap_region2 = cms.double( 0.6 ),
    selePtPairEndCap_region2 = cms.double( 2.5 ),
    selePtGammaEndCap_region3 = cms.double( 0.6 ),
    selePtPairEndCap_region3 = cms.double( 2.5 ),
    seleS4S9GammaEndCap = cms.double( 0.9 ),
    seleS9S25GammaEndCap = cms.double( 0.0 ),
    ptMinForIsolationEndCap = cms.double( 0.5 ),
    seleBeltDREndCap = cms.double( 0.2 ),
    seleBeltDetaEndCap = cms.double( 0.05 ),
    seleIsoEndCap = cms.double( 0.5 ),
    store5x5RecHitEE = cms.bool( False ),
    endcapHitCollection = cms.string( "pi0EcalRecHitsEE" ),
    selePtPairMaxEndCap_region3 = cms.double( 2.5 )
  ),
  preshowerSelection = cms.PSet(
    preshNclust = cms.int32( 4 ),
    preshClusterEnergyCut = cms.double( 0.0 ),
    preshStripEnergyCut = cms.double( 0.0 ),
    preshSeededNstrip = cms.int32( 15 ),
    preshCalibPlaneX = cms.double( 1.0 ),
    preshCalibPlaneY = cms.double( 0.7 ),
    preshCalibGamma = cms.double( 0.024 ),
    preshCalibMIP = cms.double( 9.0e-05 ),
    debugLevelES = cms.string( "" ),
    ESCollection = cms.string( "pi0EcalRecHitsES" )
  )
)
process.hltBDiJet10U = cms.HLTFilter( "HLT1CaloBJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 10.0 ),
  MaxEta = cms.double( 3.0 ),
  MinN = cms.int32( 2 )
)
process.hltBDiJet20U = cms.HLTFilter( "HLT1CaloBJet",
  inputTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 3.0 ),
  MinN = cms.int32( 2 )
)
process.hltBPTXAntiCoincidence = cms.HLTFilter( "HLTLevel1Activity",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( True ),
  invert = cms.bool( True ),
  bunchCrossings = cms.vint32( 0, 1, -1 ),
  physicsLoBits = cms.uint64( 0x0000000000000001 ),
  physicsHiBits = cms.uint64( 0x0000000000040000 ),
  technicalBits = cms.uint64( 0x0000000000000001 )
)
process.hltBPTXCoincidence = cms.HLTFilter( "HLTLevel1Activity",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( True ),
  invert = cms.bool( False ),
  bunchCrossings = cms.vint32( 0, -1, 1 ),
  physicsLoBits = cms.uint64( 0x0000000000000001 ),
  physicsHiBits = cms.uint64( 0x0000000000040000 ),
  technicalBits = cms.uint64( 0x0000000000000001 )
)
process.hltBSoftMuonL25BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
  jetTagComputer = cms.string( "softLeptonByDistance" ),
  tagInfos = cms.VInputTag( "hltBSoftMuonL25TagInfosU" )
)
process.hltBSoftMuonL25FilterUByDR = cms.HLTFilter( "HLTJetTag",
  JetTag = cms.InputTag( "hltBSoftMuonL25BJetTagsUByDR" ),
  MinTag = cms.double( 0.5 ),
  MaxTag = cms.double( 99999.0 ),
  MinJets = cms.int32( 1 ),
  SaveTag = cms.bool( False )
)
process.hltBSoftMuonL25JetsU = cms.EDFilter( "EtMinCaloJetSelector",
  src = cms.InputTag( "hltSelector4JetsU" ),
  filter = cms.bool( False ),
  etMin = cms.double( 10.0 )
)
process.hltBSoftMuonL25TagInfosU = cms.EDProducer( "SoftLepton",
  jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
  primaryVertex = cms.InputTag( "nominal" ),
  leptons = cms.InputTag( "hltL2Muons" ),
  leptonCands = cms.InputTag( "" ),
  leptonId = cms.InputTag( "" ),
  refineJetAxis = cms.uint32( 0 ),
  leptonDeltaRCut = cms.double( 0.4 ),
  leptonChi2Cut = cms.double( 0.0 ),
  muonSelection = cms.uint32( 0 )
)
process.hltBSoftMuonL3 = cms.EDFilter( "RecoTrackRefSelector",
  src = cms.InputTag( "hltL3Muons" ),
  maxChi2 = cms.double( 10000.0 ),
  tip = cms.double( 120.0 ),
  minRapidity = cms.double( -5.0 ),
  lip = cms.double( 300.0 ),
  ptMin = cms.double( 5.0 ),
  maxRapidity = cms.double( 5.0 ),
  quality = cms.vstring(  ),
  algorithm = cms.vstring(  ),
  minHit = cms.int32( 0 ),
  min3DHit = cms.int32( 0 ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" )
)
process.hltBSoftMuonL3BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
  jetTagComputer = cms.string( "softLeptonByDistance" ),
  tagInfos = cms.VInputTag( "hltBSoftMuonL3TagInfosU" )
)
process.hltBSoftMuonL3BJetTagsUByPt = cms.EDProducer( "JetTagProducer",
  jetTagComputer = cms.string( "softLeptonByPt" ),
  tagInfos = cms.VInputTag( "hltBSoftMuonL3TagInfosU" )
)
process.hltBSoftMuonL3FilterUByDR = cms.HLTFilter( "HLTJetTag",
  JetTag = cms.InputTag( "hltBSoftMuonL3BJetTagsUByDR" ),
  MinTag = cms.double( 0.5 ),
  MaxTag = cms.double( 99999.0 ),
  MinJets = cms.int32( 1 ),
  SaveTag = cms.bool( True )
)
process.hltBSoftMuonL3TagInfosU = cms.EDProducer( "SoftLepton",
  jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
  primaryVertex = cms.InputTag( "nominal" ),
  leptons = cms.InputTag( "hltL3Muons" ),
  leptonCands = cms.InputTag( "" ),
  leptonId = cms.InputTag( "" ),
  refineJetAxis = cms.uint32( 0 ),
  leptonDeltaRCut = cms.double( 0.4 ),
  leptonChi2Cut = cms.double( 0.0 ),
  muonSelection = cms.uint32( 0 )
)
process.hltBSoftMuonSelL3BJetTagsUByDR = cms.EDProducer( "JetTagProducer",
  jetTagComputer = cms.string( "softLeptonByDistance" ),
  tagInfos = cms.VInputTag( "hltBSoftMuonSelL3TagInfosU" )
)
process.hltBSoftMuonSelL3BJetTagsUByPt = cms.EDProducer( "JetTagProducer",
  jetTagComputer = cms.string( "softLeptonByPt" ),
  tagInfos = cms.VInputTag( "hltBSoftMuonSelL3TagInfosU" )
)
process.hltBSoftMuonSelL3FilterUByDR = cms.HLTFilter( "HLTJetTag",
  JetTag = cms.InputTag( "hltBSoftMuonSelL3BJetTagsUByDR" ),
  MinTag = cms.double( 0.5 ),
  MaxTag = cms.double( 99999.0 ),
  MinJets = cms.int32( 1 ),
  SaveTag = cms.bool( True )
)
process.hltBSoftMuonSelL3TagInfosU = cms.EDProducer( "SoftLepton",
  jets = cms.InputTag( "hltBSoftMuonL25JetsU" ),
  primaryVertex = cms.InputTag( "nominal" ),
  leptons = cms.InputTag( "hltBSoftMuonL3" ),
  leptonCands = cms.InputTag( "" ),
  leptonId = cms.InputTag( "" ),
  refineJetAxis = cms.uint32( 0 ),
  leptonDeltaRCut = cms.double( 0.4 ),
  leptonChi2Cut = cms.double( 0.0 ),
  muonSelection = cms.uint32( 0 )
)
process.hltBoolEnd = cms.HLTFilter( "HLTBool",
  result = cms.bool( True )
)
process.hltBoolFalse = cms.HLTFilter( "HLTBool",
  result = cms.bool( False )
)
process.hltBoolTrue = cms.HLTFilter( "HLTBool",
  result = cms.bool( True )
)
process.hltCSCActivityFilter = cms.HLTFilter( "HLTCSCActivityFilter",
  cscStripDigiTag = cms.InputTag( "hltMuonCSCDigis:MuonCSCStripDigi" ),
  applyfilter = cms.bool( True ),
  skipStationRing = cms.bool( True ),
  skipRingNumber = cms.int32( 4 ),
  skipStationNumber = cms.int32( 1 )
)
process.hltCalibrationEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 2 )
)
process.hltCaloTowersCentral1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Central" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 0 )
)
process.hltCaloTowersCentral2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Central" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 1 )
)
process.hltCaloTowersCentral3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Central" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 2 )
)
process.hltCaloTowersCentral4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Central" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 3 )
)
process.hltCaloTowersTau1Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Tau" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 0 )
)
process.hltCaloTowersTau2Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Tau" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 1 )
)
process.hltCaloTowersTau3Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Tau" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 2 )
)
process.hltCaloTowersTau4Regional = cms.EDProducer( "CaloTowerCreatorForTauHLT",
  verbose = cms.untracked.int32( 0 ),
  towers = cms.InputTag( "hltTowerMakerForJets" ),
  UseTowersInCone = cms.double( 0.8 ),
  TauTrigger = cms.InputTag( "hltL1extraParticles:Tau" ),
  minimumEt = cms.double( 0.5 ),
  minimumE = cms.double( 0.8 ),
  TauId = cms.int32( 3 )
)
process.hltCkfL1IsoStartUpWindowTrackCandidatesLowPt = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1IsoStartUpElectronPixelSeedsLowPt" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltCkfL1IsoTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltCkfL1NonIsoStartUpWindowTrackCandidatesLowPt = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeedsLowPt" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltCkfL1NonIsoTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltCorrectedHybridSuperClustersActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersActivity" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 0.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fBremVec = cms.vdouble( -0.04382, 0.1169, 0.9267, -0.0009413, 1.419 ),
    brLinearHighThr = cms.double( 8.0 ),
    fEtEtaVec = cms.vdouble( 0.0, 1.00121, -0.63672, 0.0, 0.0, 0.0, 0.5655, 6.457, 0.5081, 8.0, 1.023, -0.00181 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1Isolated" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
    brLinearHighThr = cms.double( 8.0 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedHybridSuperClustersL1IsolatedLowPt = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1IsolatedLowPt" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
    brLinearHighThr = cms.double( 8.0 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedTemp" ),
  L1IsoSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedHybridSuperClustersL1NonIsolatedLowPt = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedTempLowPt" ),
  L1IsoSC = cms.InputTag( "hltCorrectedHybridSuperClustersL1IsolatedLowPt" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1NonIsolated" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
    brLinearHighThr = cms.double( 8.0 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedHybridSuperClustersL1NonIsolatedTempLowPt = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  rawSuperClusterProducer = cms.InputTag( "hltHybridSuperClustersL1NonIsolatedLowPt" ),
  superClusterAlgo = cms.string( "Hybrid" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.03 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 1.1 ),
    fEtEtaVec = cms.vdouble( 1.0012, -0.5714, 0.0, 0.0, 0.0, 0.5549, 12.74, 1.0448, 0.0, 0.0, 0.0, 0.0, 8.0, 1.023, -0.00181, 0.0, 0.0 ),
    brLinearHighThr = cms.double( 8.0 ),
    fBremVec = cms.vdouble( -0.05208, 0.1331, 0.9196, -0.0005735, 1.343 )
  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(

  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
    brLinearHighThr = cms.double( 6.0 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
    brLinearHighThr = cms.double( 6.0 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp" ),
  L1IsoSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt = cms.EDProducer( "EgammaHLTRemoveDuplicatedSC",
  L1NonIsoUskimmedSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTempLowPt" ),
  L1IsoSC = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt" ),
  L1NonIsoSkimmedCollection = cms.string( "" )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
    brLinearHighThr = cms.double( 6.0 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
  )
)
process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTempLowPt = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 1.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.6 ),
    fEtEtaVec = cms.vdouble( 0.9746, -6.512, 0.0, 0.0, 0.02771, 4.983, 0.0, 0.0, -0.007288, -0.9446, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0 ),
    brLinearHighThr = cms.double( 6.0 ),
    fBremVec = cms.vdouble( -0.04163, 0.08552, 0.95048, -0.002308, 1.077 )
  )
)
process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "EgammaSCCorrectionMaker",
  VerbosityLevel = cms.string( "ERROR" ),
  recHitProducer = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  rawSuperClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersWithPreshowerActivity" ),
  superClusterAlgo = cms.string( "Multi5x5" ),
  applyEnergyCorrection = cms.bool( True ),
  sigmaElectronicNoise = cms.double( 0.15 ),
  etThresh = cms.double( 0.0 ),
  corectedSuperClusterCollection = cms.string( "" ),
  hyb_fCorrPset = cms.PSet(

  ),
  isl_fCorrPset = cms.PSet(

  ),
  dyn_fCorrPset = cms.PSet(

  ),
  fix_fCorrPset = cms.PSet(
    brLinearLowThr = cms.double( 0.9 ),
    fBremVec = cms.vdouble( -0.05228, 0.08738, 0.9508, 0.002677, 1.221 ),
    brLinearHighThr = cms.double( 6.0 ),
    fEtEtaVec = cms.vdouble( 1.0, -0.4386, -32.38, 0.6372, 15.67, -0.0928, -2.462, 1.138, 20.93 )
  )
)
process.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
  CSCUseCalibrations = cms.bool( True ),
  CSCUseStaticPedestals = cms.bool( False ),
  CSCUseTimingCorrections = cms.bool( True ),
  stripDigiTag = cms.InputTag( "hltMuonCSCDigis:MuonCSCStripDigi" ),
  wireDigiTag = cms.InputTag( "hltMuonCSCDigis:MuonCSCWireDigi" ),
  CSCstripWireDeltaTime = cms.int32( 8 ),
  CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
  CSCStripPeakThreshold = cms.double( 10.0 ),
  CSCStripClusterChargeCut = cms.double( 25.0 ),
  CSCWireClusterDeltaT = cms.int32( 1 ),
  CSCStripxtalksOffset = cms.double( 0.03 ),
  NoiseLevel_ME1a = cms.double( 7.0 ),
  XTasymmetry_ME1a = cms.double( 0.0 ),
  ConstSyst_ME1a = cms.double( 0.022 ),
  NoiseLevel_ME1b = cms.double( 8.0 ),
  XTasymmetry_ME1b = cms.double( 0.0 ),
  ConstSyst_ME1b = cms.double( 0.007 ),
  NoiseLevel_ME12 = cms.double( 9.0 ),
  XTasymmetry_ME12 = cms.double( 0.0 ),
  ConstSyst_ME12 = cms.double( 0.0 ),
  NoiseLevel_ME13 = cms.double( 8.0 ),
  XTasymmetry_ME13 = cms.double( 0.0 ),
  ConstSyst_ME13 = cms.double( 0.0 ),
  NoiseLevel_ME21 = cms.double( 9.0 ),
  XTasymmetry_ME21 = cms.double( 0.0 ),
  ConstSyst_ME21 = cms.double( 0.0 ),
  NoiseLevel_ME22 = cms.double( 9.0 ),
  XTasymmetry_ME22 = cms.double( 0.0 ),
  ConstSyst_ME22 = cms.double( 0.0 ),
  NoiseLevel_ME31 = cms.double( 9.0 ),
  XTasymmetry_ME31 = cms.double( 0.0 ),
  ConstSyst_ME31 = cms.double( 0.0 ),
  NoiseLevel_ME32 = cms.double( 9.0 ),
  XTasymmetry_ME32 = cms.double( 0.0 ),
  ConstSyst_ME32 = cms.double( 0.0 ),
  NoiseLevel_ME41 = cms.double( 9.0 ),
  XTasymmetry_ME41 = cms.double( 0.0 ),
  ConstSyst_ME41 = cms.double( 0.0 ),
  readBadChannels = cms.bool( True ),
  readBadChambers = cms.bool( True ),
  UseAverageTime = cms.bool( False ),
  UseParabolaFit = cms.bool( False ),
  UseFivePoleFit = cms.bool( True )
)
process.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
  inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
  algo_type = cms.int32( 1 ),
  algo_psets = cms.VPSet(
    cms.PSet(
      chamber_types = cms.vstring( "ME1/a", "ME1/b", "ME1/2", "ME1/3", "ME2/1", "ME2/2", "ME3/1", "ME3/2", "ME4/1", "ME4/2" ),
      algo_name = cms.string( "CSCSegAlgoST" ),
      algo_psets = cms.VPSet(
        cms.PSet(
          maxRatioResidualPrune = cms.double( 3.0 ),
          yweightPenalty = cms.double( 1.5 ),
          maxRecHitsInCluster = cms.int32( 20 ),
          hitDropLimit6Hits = cms.double( 0.3333 ),
          BPMinImprovement = cms.double( 10000.0 ),
          tanPhiMax = cms.double( 0.5 ),
          onlyBestSegment = cms.bool( False ),
          dRPhiFineMax = cms.double( 8.0 ),
          curvePenalty = cms.double( 2.0 ),
          dXclusBoxMax = cms.double( 4.0 ),
          BrutePruning = cms.bool( True ),
          tanThetaMax = cms.double( 1.2 ),
          hitDropLimit4Hits = cms.double( 0.6 ),
          useShowering = cms.bool( False ),
          CSCDebug = cms.untracked.bool( False ),
          curvePenaltyThreshold = cms.double( 0.85 ),
          minHitsPerSegment = cms.int32( 3 ),
          dPhiFineMax = cms.double( 0.025 ),
          yweightPenaltyThreshold = cms.double( 1.0 ),
          hitDropLimit5Hits = cms.double( 0.8 ),
          preClustering = cms.bool( True ),
          maxDPhi = cms.double( 999.0 ),
          maxDTheta = cms.double( 999.0 ),
          Pruning = cms.bool( True ),
          dYclusBoxMax = cms.double( 8.0 ),
          preClusteringUseChaining = cms.bool( True ),
          CorrectTheErrors = cms.bool( True ),
          NormChi2Cut2D = cms.double( 20.0 ),
          NormChi2Cut3D = cms.double( 10.0 ),
          prePrun = cms.bool( True ),
          prePrunLimit = cms.double( 3.17 ),
          SeedSmall = cms.double( 0.0002 ),
          SeedBig = cms.double( 0.0015 ),
          ForceCovariance = cms.bool( False ),
          ForceCovarianceAll = cms.bool( False ),
          Covariance = cms.double( 0.0 )
        ),
        cms.PSet(
          maxRatioResidualPrune = cms.double( 3.0 ),
          yweightPenalty = cms.double( 1.5 ),
          maxRecHitsInCluster = cms.int32( 24 ),
          hitDropLimit6Hits = cms.double( 0.3333 ),
          BPMinImprovement = cms.double( 10000.0 ),
          tanPhiMax = cms.double( 0.5 ),
          onlyBestSegment = cms.bool( False ),
          dRPhiFineMax = cms.double( 8.0 ),
          curvePenalty = cms.double( 2.0 ),
          dXclusBoxMax = cms.double( 4.0 ),
          BrutePruning = cms.bool( True ),
          tanThetaMax = cms.double( 1.2 ),
          hitDropLimit4Hits = cms.double( 0.6 ),
          useShowering = cms.bool( False ),
          CSCDebug = cms.untracked.bool( False ),
          curvePenaltyThreshold = cms.double( 0.85 ),
          minHitsPerSegment = cms.int32( 3 ),
          dPhiFineMax = cms.double( 0.025 ),
          yweightPenaltyThreshold = cms.double( 1.0 ),
          hitDropLimit5Hits = cms.double( 0.8 ),
          preClustering = cms.bool( True ),
          maxDPhi = cms.double( 999.0 ),
          maxDTheta = cms.double( 999.0 ),
          Pruning = cms.bool( True ),
          dYclusBoxMax = cms.double( 8.0 ),
          preClusteringUseChaining = cms.bool( True ),
          CorrectTheErrors = cms.bool( True ),
          NormChi2Cut2D = cms.double( 20.0 ),
          NormChi2Cut3D = cms.double( 10.0 ),
          prePrun = cms.bool( True ),
          prePrunLimit = cms.double( 3.17 ),
          SeedSmall = cms.double( 0.0002 ),
          SeedBig = cms.double( 0.0015 ),
          ForceCovariance = cms.bool( False ),
          ForceCovarianceAll = cms.bool( False ),
          Covariance = cms.double( 0.0 )
        )
      ),
      parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 )
    )
  )
)
process.hltCtfL1IsoStartUpWindowWithMaterialTracksLowPt = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracksLowPt" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltCkfL1IsoStartUpWindowTrackCandidatesLowPt" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltCtfL1IsoWithMaterialTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracks" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltCkfL1IsoTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltCtfL1NonIsoStartUpWindowWithMaterialTracksLowPt = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracksLowPt" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltCkfL1NonIsoStartUpWindowTrackCandidatesLowPt" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltCtfL1NonIsoWithMaterialTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracks" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltCkfL1NonIsoTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltDQMHLTScalers = cms.EDAnalyzer( "HLTScalers",
  dqmFolder = cms.untracked.string( "HLT/HLTScalers_EvF" ),
  triggerResults = cms.InputTag( "TriggerResults::HLT" ),
  MonitorDaemon = cms.untracked.bool( False )
)
process.hltDQML1Scalers = cms.EDAnalyzer( "L1Scalers",
  verbose = cms.untracked.bool( False ),
  l1GtData = cms.InputTag( "hltGtDigis" ),
  denomIsTech = cms.untracked.bool( True ),
  denomBit = cms.untracked.uint32( 40 ),
  tfIsTech = cms.untracked.bool( True ),
  tfBit = cms.untracked.uint32( 41 ),
  dqmFolder = cms.untracked.string( "L1T/L1Scalers_EvF" ),
  firstFED = cms.untracked.uint32( 0 ),
  lastFED = cms.untracked.uint32( 931 ),
  fedRawData = cms.InputTag( "source" ),
  HFRecHitCollection = cms.InputTag( "hltHfreco" ),
  algoMonitorBits = cms.untracked.vuint32(  ),
  techMonitorBits = cms.untracked.vuint32(  ),
  maskedChannels = cms.untracked.vint32( 8137, 8141, 8146, 8149, 8150, 8153 )
)
process.hltDQML1SeedLogicScalers = cms.EDAnalyzer( "HLTSeedL1LogicScalers",
  l1BeforeMask = cms.bool( False ),
  processname = cms.string( "HLT" ),
  L1GtDaqReadoutRecordInputTag = cms.InputTag( "hltGtDigis" ),
  L1GtRecordInputTag = cms.InputTag( "unused" ),
  DQMFolder = cms.untracked.string( "HLT/HLTSeedL1LogicScalers_EvF" ),
  monitorPaths = cms.untracked.vstring( "HLT_L1MuOpen", "HLT_L1Mu", "HLT_Mu3", "HLT_L1SingleForJet", "HLT_SingleLooseIsoTau20", "HLT_MinBiasEcal" )
)
process.hltDTActivityFilter = cms.HLTFilter( "HLTDTActivityFilter",
  inputDCC = cms.InputTag( "hltDTTFUnpacker" ),
  inputDDU = cms.InputTag( "hltMuonDTDigis" ),
  inputRPC = cms.InputTag( "hltGtDigis" ),
  inputDigis = cms.InputTag( "hltMuonDTDigis" ),
  processDCC = cms.bool( True ),
  processDDU = cms.bool( True ),
  processRPC = cms.bool( True ),
  processDigis = cms.bool( True ),
  orTPG = cms.bool( True ),
  orRPC = cms.bool( True ),
  orDigi = cms.bool( False ),
  minDCCBX = cms.int32( -1 ),
  maxDCCBX = cms.int32( 1 ),
  minDDUBX = cms.int32( 8 ),
  maxDDUBX = cms.int32( 13 ),
  minRPCBX = cms.int32( -1 ),
  maxRPCBX = cms.int32( 1 ),
  minTPGQual = cms.int32( 2 ),
  maxStation = cms.int32( 3 ),
  minChamberLayers = cms.int32( 5 ),
  minActiveChambs = cms.int32( 1 ),
  maxDeltaPhi = cms.double( 1.0 ),
  maxDeltaEta = cms.double( 0.3 ),
  activeSectors = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 )
)
process.hltDTActivityFilterTuned = cms.HLTFilter( "HLTDTActivityFilter",
  inputDCC = cms.InputTag( "hltDTTFUnpacker" ),
  inputDDU = cms.InputTag( "hltMuonDTDigis" ),
  inputRPC = cms.InputTag( "hltGtDigis" ),
  inputDigis = cms.InputTag( "hltMuonDTDigis" ),
  processDCC = cms.bool( True ),
  processDDU = cms.bool( True ),
  processRPC = cms.bool( True ),
  processDigis = cms.bool( True ),
  orTPG = cms.bool( True ),
  orRPC = cms.bool( True ),
  orDigi = cms.bool( False ),
  minDCCBX = cms.int32( -1 ),
  maxDCCBX = cms.int32( 1 ),
  minDDUBX = cms.int32( 8 ),
  maxDDUBX = cms.int32( 13 ),
  minRPCBX = cms.int32( -1 ),
  maxRPCBX = cms.int32( 1 ),
  minTPGQual = cms.int32( 2 ),
  maxStation = cms.int32( 3 ),
  minChamberLayers = cms.int32( 5 ),
  minActiveChambs = cms.int32( 1 ),
  maxDeltaPhi = cms.double( 1.0 ),
  maxDeltaEta = cms.double( 0.3 ),
  activeSectors = cms.vint32( 1, 12 )
)
process.hltDTDQMEvF = cms.EDProducer( "DTUnpackingModule",
  dataType = cms.string( "DDU" ),
  fedbyType = cms.bool( False ),
  inputLabel = cms.InputTag( "source" ),
  useStandardFEDid = cms.bool( True ),
  minFEDid = cms.untracked.int32( 770 ),
  maxFEDid = cms.untracked.int32( 779 ),
  dqmOnly = cms.bool( False ),
  rosParameters = cms.PSet(

  ),
  readOutParameters = cms.PSet(
    debug = cms.untracked.bool( False ),
    rosParameters = cms.PSet(
      writeSC = cms.untracked.bool( True ),
      readingDDU = cms.untracked.bool( True ),
      performDataIntegrityMonitor = cms.untracked.bool( True ),
      readDDUIDfromDDU = cms.untracked.bool( True ),
      debug = cms.untracked.bool( False ),
      localDAQ = cms.untracked.bool( False )
    ),
    performDataIntegrityMonitor = cms.untracked.bool( True ),
    localDAQ = cms.untracked.bool( False )
  )
)
process.hltDTROMonitorFilter = cms.HLTFilter( "HLTDTROMonitorFilter",
  inputLabel = cms.InputTag( "source" )
)
process.hltDTTFUnpacker = cms.EDProducer( "DTTFFEDReader",
  DTTF_FED_Source = cms.InputTag( "source" ),
  verbose = cms.untracked.bool( False )
)
process.hltDiJetAve100U = cms.HLTFilter( "HLTDiJetAveFilter",
  inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  minPtAve = cms.double( 100.0 ),
  minPtJet3 = cms.double( 99999.0 ),
  minDphi = cms.double( -1.0 )
)
process.hltDiJetAve15U = cms.HLTFilter( "HLTDiJetAveFilter",
  inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  minPtAve = cms.double( 15.0 ),
  minPtJet3 = cms.double( 99999.0 ),
  minDphi = cms.double( -1.0 )
)
process.hltDiJetAve30U = cms.HLTFilter( "HLTDiJetAveFilter",
  inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  minPtAve = cms.double( 30.0 ),
  minPtJet3 = cms.double( 99999.0 ),
  minDphi = cms.double( -1.0 )
)
process.hltDiJetAve50U = cms.HLTFilter( "HLTDiJetAveFilter",
  inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  minPtAve = cms.double( 50.0 ),
  minPtJet3 = cms.double( 99999.0 ),
  minDphi = cms.double( -1.0 )
)
process.hltDiJetAve70U = cms.HLTFilter( "HLTDiJetAveFilter",
  inputJetTag = cms.InputTag( "hltIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  minPtAve = cms.double( 70.0 ),
  minPtJet3 = cms.double( 99999.0 ),
  minDphi = cms.double( -1.0 )
)
process.hltDiMuonL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpen" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 2 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltDiMuonL2PreFiltered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered0 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDiMuonL3PreFiltered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDoubleJet15UForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
  inputTag = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
  saveTag = cms.untracked.bool( True ),
  minPt = cms.double( 15.0 ),
  minEta = cms.double( 3.0 ),
  maxEta = cms.double( 5.1 )
)
process.hltDoubleJet25UForwardBackward = cms.HLTFilter( "HLTForwardBackwardJetsFilter",
  inputTag = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
  saveTag = cms.untracked.bool( True ),
  minPt = cms.double( 25.0 ),
  minEta = cms.double( 3.0 ),
  maxEta = cms.double( 5.1 )
)
process.hltDoubleMu0QuarkoniumL3PreFiltered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  FastAccept = cms.bool( False ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  ChargeOpt = cms.int32( -1 ),
  MinPtPair = cms.double( 0.0 ),
  MinPtMax = cms.double( 0.0 ),
  MinPtMin = cms.double( 0.0 ),
  MinInvMass = cms.double( 1.5 ),
  MaxInvMass = cms.double( 14.5 ),
  MinAcop = cms.double( -999.0 ),
  MaxAcop = cms.double( 999.0 ),
  MinPtBalance = cms.double( -1.0 ),
  MaxPtBalance = cms.double( 999999.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDoubleMu0QuarkoniumLSL3PreFiltered = cms.HLTFilter( "HLTMuonDimuonL3Filter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  FastAccept = cms.bool( False ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  ChargeOpt = cms.int32( 1 ),
  MinPtPair = cms.double( 0.0 ),
  MinPtMax = cms.double( 0.0 ),
  MinPtMin = cms.double( 0.0 ),
  MinInvMass = cms.double( 1.5 ),
  MaxInvMass = cms.double( 14.5 ),
  MinAcop = cms.double( -999.0 ),
  MaxAcop = cms.double( 999.0 ),
  MinPtBalance = cms.double( -1.0 ),
  MaxPtBalance = cms.double( 999999.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltDoubleMuLevel1PathL1OpenFiltered = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1DoubleMuOpen" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 2 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltDoublePhotonEt5EcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltDoublePhotonEt5EtPhiFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 3.0 ),
  thrRegularEE = cms.double( 3.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltDoublePhotonEt5EtPhiFilter = cms.HLTFilter( "HLTEgammaDoubleEtDeltaPhiFilter",
  inputTag = cms.InputTag( "hltDoublePhotonEt5L1MatchFilterRegional" ),
  etcut = cms.double( 5.0 ),
  minDeltaPhi = cms.double( 2.5 ),
  saveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltDoublePhotonEt5HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltDoublePhotonEt5EcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltDoublePhotonEt5L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
  debug = cms.untracked.bool( False ),
  dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
  recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
  recAlgoConfig = cms.PSet(
    debug = cms.untracked.bool( False ),
    minTime = cms.double( -3.0 ),
    maxTime = cms.double( 420.0 ),
    tTrigModeConfig = cms.PSet(
      vPropWire = cms.double( 24.4 ),
      doTOFCorrection = cms.bool( True ),
      tofCorrType = cms.int32( 0 ),
      wirePropCorrType = cms.int32( 0 ),
      doWirePropCorrection = cms.bool( True ),
      doT0Correction = cms.bool( True ),
      debug = cms.untracked.bool( False ),
      tTrigLabel = cms.string( "" )
    ),
    tTrigMode = cms.string( "DTTTrigSyncFromDB" )
  )
)
process.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
  debug = cms.untracked.bool( False ),
  recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
  recHits2DLabel = cms.InputTag( "dt2DSegments" ),
  Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
  Reco4DAlgoConfig = cms.PSet(
    segmCleanerMode = cms.int32( 2 ),
    Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
    nSharedHitsMax = cms.int32( 2 ),
    hit_afterT0_resolution = cms.double( 0.03 ),
    Reco2DAlgoConfig = cms.PSet(
      segmCleanerMode = cms.int32( 2 ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      nSharedHitsMax = cms.int32( 2 ),
      AlphaMaxPhi = cms.double( 1.0 ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      MaxAllowedHits = cms.uint32( 50 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      AlphaMaxTheta = cms.double( 0.9 ),
      debug = cms.untracked.bool( False ),
      recAlgoConfig = cms.PSet(
        debug = cms.untracked.bool( False ),
        minTime = cms.double( -3.0 ),
        maxTime = cms.double( 420.0 ),
        tTrigModeConfig = cms.PSet(
          vPropWire = cms.double( 24.4 ),
          doTOFCorrection = cms.bool( True ),
          tofCorrType = cms.int32( 0 ),
          wirePropCorrType = cms.int32( 0 ),
          doWirePropCorrection = cms.bool( True ),
          doT0Correction = cms.bool( True ),
          debug = cms.untracked.bool( False ),
          tTrigLabel = cms.string( "" )
        ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False )
    ),
    performT0_vdriftSegCorrection = cms.bool( False ),
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet(
      debug = cms.untracked.bool( False ),
      minTime = cms.double( -3.0 ),
      maxTime = cms.double( 420.0 ),
      tTrigModeConfig = cms.PSet(
        vPropWire = cms.double( 24.4 ),
        doTOFCorrection = cms.bool( True ),
        tofCorrType = cms.int32( 0 ),
        wirePropCorrType = cms.int32( 0 ),
        doWirePropCorrection = cms.bool( True ),
        doT0Correction = cms.bool( True ),
        debug = cms.untracked.bool( False ),
        tTrigLabel = cms.string( "" )
      ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" )
    ),
    nUnSharedHitsMin = cms.int32( 2 ),
    AllDTRecHits = cms.bool( True ),
    performT0SegCorrection = cms.bool( False )
  )
)
process.hltDynAlCaDTErrors = cms.HLTFilter( "HLTDynamicPrescaler" )
process.hltEBHltTask = cms.EDAnalyzer( "EBHltTask",
  prefixME = cms.untracked.string( "EcalBarrel" ),
  folderName = cms.untracked.string( "FEDIntegrity" ),
  enableCleanup = cms.untracked.bool( False ),
  mergeRuns = cms.untracked.bool( False ),
  EBDetIdCollection0 = cms.InputTag( "hltEcalDigis:EcalIntegrityDCCSizeErrors" ),
  EBDetIdCollection1 = cms.InputTag( "hltEcalDigis:EcalIntegrityGainErrors" ),
  EBDetIdCollection2 = cms.InputTag( "hltEcalDigis:EcalIntegrityChIdErrors" ),
  EBDetIdCollection3 = cms.InputTag( "hltEcalDigis:EcalIntegrityGainSwitchErrors" ),
  EcalElectronicsIdCollection1 = cms.InputTag( "hltEcalDigis:EcalIntegrityTTIdErrors" ),
  EcalElectronicsIdCollection2 = cms.InputTag( "hltEcalDigis:EcalIntegrityBlockSizeErrors" ),
  EcalElectronicsIdCollection3 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemTtIdErrors" ),
  EcalElectronicsIdCollection4 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemBlockSizeErrors" ),
  EcalElectronicsIdCollection5 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemChIdErrors" ),
  EcalElectronicsIdCollection6 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemGainErrors" ),
  FEDRawDataCollection = cms.InputTag( "source" )
)
process.hltEEHltTask = cms.EDAnalyzer( "EEHltTask",
  prefixME = cms.untracked.string( "EcalEndcap" ),
  folderName = cms.untracked.string( "FEDIntegrity" ),
  enableCleanup = cms.untracked.bool( False ),
  mergeRuns = cms.untracked.bool( False ),
  EEDetIdCollection0 = cms.InputTag( "hltEcalDigis:EcalIntegrityDCCSizeErrors" ),
  EEDetIdCollection1 = cms.InputTag( "hltEcalDigis:EcalIntegrityGainErrors" ),
  EEDetIdCollection2 = cms.InputTag( "hltEcalDigis:EcalIntegrityChIdErrors" ),
  EEDetIdCollection3 = cms.InputTag( "hltEcalDigis:EcalIntegrityGainSwitchErrors" ),
  EcalElectronicsIdCollection1 = cms.InputTag( "hltEcalDigis:EcalIntegrityTTIdErrors" ),
  EcalElectronicsIdCollection2 = cms.InputTag( "hltEcalDigis:EcalIntegrityBlockSizeErrors" ),
  EcalElectronicsIdCollection3 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemTtIdErrors" ),
  EcalElectronicsIdCollection4 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemBlockSizeErrors" ),
  EcalElectronicsIdCollection5 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemChIdErrors" ),
  EcalElectronicsIdCollection6 = cms.InputTag( "hltEcalDigis:EcalIntegrityMemGainErrors" ),
  FEDRawDataCollection = cms.InputTag( "source" )
)
process.hltESRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
  sourceTag = cms.InputTag( "source" ),
  workerName = cms.string( "esRawToRecHit" )
)
process.hltESRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalESRestFEDs:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDs:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalEgammaRecHitLowPt = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDsLowPt:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltESRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltESRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalPi0EtaFEDs:es" ),
  splitOutput = cms.bool( False ),
  EBrechitCollection = cms.string( "" ),
  EErechitCollection = cms.string( "" ),
  rechitCollection = cms.string( "EcalRecHitsES" )
)
process.hltEcalActivitySuperClusterWrapper = cms.HLTFilter( "HLTEgammaTriggerFilterObjectWrapper",
  candIsolatedTag = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  candNonIsolatedTag = cms.InputTag( "none" ),
  doIsolated = cms.bool( True )
)
process.hltEcalCalibrationRaw = cms.EDProducer( "EvFFEDSelector",
  inputTag = cms.InputTag( "source" ),
  fedList = cms.vuint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
  numbXtalTSamples = cms.int32( 10 ),
  numbTriggerTSamples = cms.int32( 1 ),
  headerUnpacking = cms.bool( True ),
  srpUnpacking = cms.bool( False ),
  tccUnpacking = cms.bool( False ),
  feUnpacking = cms.bool( True ),
  memUnpacking = cms.bool( True ),
  syncCheck = cms.bool( False ),
  feIdCheck = cms.bool( True ),
  forceToKeepFRData = cms.bool( False ),
  eventPut = cms.bool( True ),
  InputLabel = cms.string( "source" ),
  DoRegional = cms.bool( False ),
  FedLabel = cms.InputTag( "listfeds" ),
  silentMode = cms.untracked.bool( True ),
  FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
  orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
  orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 )
)
process.hltEcalOnlyMet = cms.EDProducer( "METProducer",
  src = cms.InputTag( "hltTowerMakerForEcalBarrelOnly" ),
  InputType = cms.string( "CandidateCollection" ),
  METType = cms.string( "CaloMET" ),
  alias = cms.string( "RawCaloMET" ),
  globalThreshold = cms.double( 0.2 ),
  noHF = cms.bool( False ),
  calculateSignificance = cms.bool( False ),
  onlyFiducialParticles = cms.bool( False ),
  usePt = cms.untracked.bool( False ),
  rf_type = cms.int32( 0 ),
  correctShowerTracks = cms.bool( False ),
  HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
  HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
  HB_PhiResPar = cms.vdouble( 0.02511 ),
  HE_PhiResPar = cms.vdouble( 0.02511 ),
  EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  EB_PhiResPar = cms.vdouble( 0.00502 ),
  EE_PhiResPar = cms.vdouble( 0.02511 ),
  HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
  EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  HF_PhiResPar = cms.vdouble( 0.05022 ),
  HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
  HO_PhiResPar = cms.vdouble( 0.02511 )
)
process.hltEcalRawToRecHitFacility = cms.EDProducer( "EcalRawToRecHitFacility",
  sourceTag = cms.InputTag( "source" ),
  workerName = cms.string( "" )
)
process.hltEcalRecHitAll = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalRestFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalESRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "all" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalEgammaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "egamma" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Isolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 5.0 ),
      regionEtaMargin = cms.double( 0.25 )
    ),
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 5.0 ),
      regionEtaMargin = cms.double( 0.25 )
    )
  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalEgammaFEDsLowPt = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "egamma" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Isolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 3.0 ),
      regionEtaMargin = cms.double( 0.25 )
    ),
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 3.0 ),
      regionEtaMargin = cms.double( 0.25 )
    )
  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalEgammaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalEgammaRecHitLowPt = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalEgammaFEDsLowPt" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalJetsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "jet" ),
  doES = cms.bool( False ),
  sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Central" ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 14.0 ),
      regionEtaMargin = cms.double( 1.0 )
    ),
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Forward" ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 20.0 ),
      regionEtaMargin = cms.double( 1.0 )
    ),
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Tau" ),
      regionPhiMargin = cms.double( 1.0 ),
      Ptmin = cms.double( 14.0 ),
      regionEtaMargin = cms.double( 1.0 )
    )
  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalJetsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalJetsFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalMuonsFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "candidate" ),
  doES = cms.bool( False ),
  sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(
    cms.PSet(
      bePrecise = cms.bool( False ),
      propagatorNameToBePrecise = cms.string( "" ),
      epsilon = cms.double( 0.01 ),
      regionPhiMargin = cms.double( 0.3 ),
      cType = cms.string( "chargedcandidate" ),
      Source = cms.InputTag( "hltL2MuonCandidates" ),
      Ptmin = cms.double( 0.0 ),
      regionEtaMargin = cms.double( 0.3 )
    )
  )
)
process.hltEcalRegionalMuonsRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalMuonsFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "NotNeededsplitOutputTrue" )
)
process.hltEcalRegionalPi0EtaFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "egamma" ),
  doES = cms.bool( True ),
  sourceTag_es = cms.InputTag( "hltESRawToRecHitFacility" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:Isolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 2.0 ),
      regionEtaMargin = cms.double( 0.25 )
    ),
    cms.PSet(
      Source = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
      regionPhiMargin = cms.double( 0.4 ),
      Ptmin = cms.double( 2.0 ),
      regionEtaMargin = cms.double( 0.25 )
    )
  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEcalRegionalPi0EtaRecHit = cms.EDProducer( "EcalRawToRecHitProducer",
  lazyGetterTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  sourceTag = cms.InputTag( "hltEcalRegionalPi0EtaFEDs" ),
  splitOutput = cms.bool( True ),
  EBrechitCollection = cms.string( "EcalRecHitsEB" ),
  EErechitCollection = cms.string( "EcalRecHitsEE" ),
  rechitCollection = cms.string( "" )
)
process.hltEcalRegionalRestFEDs = cms.EDProducer( "EcalRawToRecHitRoI",
  sourceTag = cms.InputTag( "hltEcalRawToRecHitFacility" ),
  type = cms.string( "all" ),
  doES = cms.bool( False ),
  sourceTag_es = cms.InputTag( "NotNeededoESfalse" ),
  esInstance = cms.untracked.string( "es" ),
  MuJobPSet = cms.PSet(

  ),
  JetJobPSet = cms.VPSet(

  ),
  EmJobPSet = cms.VPSet(

  ),
  CandJobPSet = cms.VPSet(

  )
)
process.hltEgammaEcalActivityR9Shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRecHitAll:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltEgammaEcalActivityR9ShapeFilterSC17 = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltEgammaSelectEcalSuperClustersActivityFilterSC17" ),
  isoTag = cms.InputTag( "hltEgammaEcalActivityR9Shape" ),
  nonIsoTag = cms.InputTag( "none" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 0.98 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "none" )
)
process.hltEgammaEcalActivityR9ShapeFilterSC7 = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltEgammaSelectEcalSuperClustersActivityFilterSC7" ),
  isoTag = cms.InputTag( "hltEgammaEcalActivityR9Shape" ),
  nonIsoTag = cms.InputTag( "none" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 0.98 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "none" )
)
process.hltEgammaSelectEcalSuperClustersActivityFilterSC17 = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "none" ),
  L1NonIsoCand = cms.InputTag( "none" )
)
process.hltEgammaSelectEcalSuperClustersActivityFilterSC7 = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 7.0 ),
  etcutEE = cms.double( 7.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "none" ),
  L1NonIsoCand = cms.InputTag( "none" )
)
process.hltElectronL1IsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
  electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  useTrackProjectionToEcal = cms.untracked.bool( False )
)
process.hltElectronL1NonIsoDetaDphi = cms.EDProducer( "EgammaHLTElectronDetaDphiProducer",
  electronProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  useTrackProjectionToEcal = cms.untracked.bool( False )
)
process.hltExclDiJet30UAND = cms.HLTFilter( "HLTExclDiJetFilter",
  inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  minPtJet = cms.double( 30.0 ),
  minHFe = cms.double( 50.0 ),
  HF_OR = cms.bool( False )
)
process.hltExclDiJet30UOR = cms.HLTFilter( "HLTExclDiJetFilter",
  inputJetTag = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  saveTag = cms.untracked.bool( True ),
  minPtJet = cms.double( 30.0 ),
  minHFe = cms.double( 50.0 ),
  HF_OR = cms.bool( True )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
  inputTag = cms.InputTag( "source" ),
  fedList = cms.vuint32( 1023 )
)
process.hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL25LeadingTrackPtCutDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL25TauLeadingTrackHighPtCutSelector" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL25LeadingTrackPtCutSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EcalIsolationDoubleIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL2EcalIsolationDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL2EcalIsolationSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EcalIsolationSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EcalIsolationSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EtCutDoubleIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL2EtCutDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL2EtCutSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EtCutSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EtCutSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2EtCutSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL2TauJets" ),
  saveTag = cms.untracked.bool( False ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL2TauMET20 = cms.HLTFilter( "HLT1CaloMET",
  inputTag = cms.InputTag( "hltMet" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL3TrackIsolationDoubleIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTDoubleIsoTau15Trk5JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 2 )
)
process.hltFilterL3TrackIsolationDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 15.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL3TrackIsolationSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTSingleIsoTau20Trk15MET20JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL3TrackIsolationSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTSingleIsoTau20Trk5MET20JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 20.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL3TrackIsolationSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTSingleIsoTau30L120or30Trk5JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLT1Tau",
  inputTag = cms.InputTag( "hltL1HLTSingleIsoTau30Trk5MET20JetsMatch" ),
  saveTag = cms.untracked.bool( True ),
  MinPt = cms.double( 30.0 ),
  MaxEta = cms.double( 5.0 ),
  MinN = cms.int32( 1 )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
  inputLabel = cms.InputTag( "source" ),
  gctFedId = cms.untracked.int32( 745 ),
  hltMode = cms.bool( True ),
  numberOfGctSamplesToUnpack = cms.uint32( 1 ),
  numberOfRctSamplesToUnpack = cms.uint32( 1 ),
  unpackSharedRegions = cms.bool( False ),
  unpackerVersion = cms.uint32( 0 ),
  checkHeaders = cms.untracked.bool( False ),
  verbose = cms.untracked.bool( False )
)
process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
  DaqGtInputTag = cms.InputTag( "source" ),
  DaqGtFedId = cms.untracked.int32( 813 ),
  ActiveBoardsMask = cms.uint32( 0x0000ffff ),
  UnpackBxInEvent = cms.int32( 5 ),
  Verbosity = cms.untracked.int32( 0 )
)
process.hltHITCkfTrackCandidatesHB8E29 = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltHITPixelTripletSeedGeneratorHB8E29" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCkfTrackCandidatesHE8E29 = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltHITPixelTripletSeedGeneratorHE8E29" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltHITCtfWithMaterialTracksHB8E29 = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHB8E29" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltHITCkfTrackCandidatesHB8E29" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltHITCtfWithMaterialTracksHE8E29 = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltHITCtfWithMaterialTracksHE8E29" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltHITCkfTrackCandidatesHE8E29" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltHITIPTCorrectorHB8E29 = cms.EDProducer( "IPTCorrector",
  corTracksLabel = cms.InputTag( "hltHITCtfWithMaterialTracksHB8E29" ),
  filterLabel = cms.InputTag( "hltIsolPixelTrackL2FilterHB8E29" ),
  associationCone = cms.double( 0.2 )
)
process.hltHITIPTCorrectorHE8E29 = cms.EDProducer( "IPTCorrector",
  corTracksLabel = cms.InputTag( "hltHITCtfWithMaterialTracksHE8E29" ),
  filterLabel = cms.InputTag( "hltIsolPixelTrackL2FilterHE8E29" ),
  associationCone = cms.double( 0.2 )
)
process.hltHITPixelTracksHB = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originRadius = cms.double( 0.0015 ),
      nSigmaZ = cms.double( 3.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.7 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    ),
    SeedingLayers = cms.string( "PixelLayerTripletsHITHB" )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    fixImpactParameter = cms.double( 0.0 )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.7 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltHITPixelTracksHE = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducerFromBeamSpot" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originRadius = cms.double( 0.0015 ),
      nSigmaZ = cms.double( 3.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.35 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    ),
    SeedingLayers = cms.string( "PixelLayerTripletsHITHE" )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByConformalMappingAndLine" ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" ),
    fixImpactParameter = cms.double( 0.0 )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.35 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltHITPixelTripletSeedGeneratorHB8E29 = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      useIsoTracks = cms.bool( True ),
      trackSrc = cms.InputTag( "hltHITPixelTracksHB" ),
      isoTrackSrc = cms.InputTag( "hltIsolPixelTrackL2FilterHB8E29" ),
      l1tjetSrc = cms.InputTag( "hltl1extraParticles:Tau" ),
      originHalfLength = cms.double( 15.0 ),
      precise = cms.bool( True ),
      deltaEtaL1JetRegion = cms.double( 0.3 ),
      useTracks = cms.bool( False ),
      originRadius = cms.double( 0.6 ),
      useL1Jets = cms.bool( False ),
      deltaPhiTrackRegion = cms.double( 0.05 ),
      deltaPhiL1JetRegion = cms.double( 0.3 ),
      vertexSrc = cms.string( "hltHITPixelVerticesHB" ),
      fixedReg = cms.bool( False ),
      etaCenter = cms.double( 0.0 ),
      phiCenter = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 ),
      deltaEtaTrackRegion = cms.double( 0.05 ),
      ptMin = cms.double( 1.0 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    ),
    SeedingLayers = cms.string( "hltPixelLayerTriplets" )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltHITPixelTripletSeedGeneratorHE8E29 = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "HITRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      useIsoTracks = cms.bool( True ),
      trackSrc = cms.InputTag( "hltHITPixelTracksHE" ),
      isoTrackSrc = cms.InputTag( "hltIsolPixelTrackL2FilterHE8E29" ),
      l1tjetSrc = cms.InputTag( "hltl1extraParticles:Tau" ),
      originHalfLength = cms.double( 15.0 ),
      precise = cms.bool( True ),
      deltaEtaL1JetRegion = cms.double( 0.3 ),
      useTracks = cms.bool( False ),
      originRadius = cms.double( 0.6 ),
      useL1Jets = cms.bool( False ),
      deltaPhiTrackRegion = cms.double( 0.05 ),
      deltaPhiL1JetRegion = cms.double( 0.3 ),
      vertexSrc = cms.string( "hltHITPixelVerticesHE" ),
      fixedReg = cms.bool( False ),
      etaCenter = cms.double( 0.0 ),
      phiCenter = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 ),
      deltaEtaTrackRegion = cms.double( 0.05 ),
      ptMin = cms.double( 0.5 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    ),
    SeedingLayers = cms.string( "hltPixelLayerTriplets" )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltHITPixelVerticesHB = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 1.0 ),
  TrackCollection = cms.InputTag( "hltHITPixelTracksHB" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltHITPixelVerticesHE = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 1.0 ),
  TrackCollection = cms.InputTag( "hltHITPixelTracksHE" ),
  beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltHT100U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 100.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT120U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 120.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT140U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 140.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT140UEta3 = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UEta3Ht" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 140.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT160U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 160.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT200U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 200.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT50U = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 50.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHT70 = cms.HLTFilter( "HLTGlobalSumsMET",
  inputTag = cms.InputTag( "hltJet20UHt" ),
  saveTag = cms.untracked.bool( True ),
  observable = cms.string( "sumEt" ),
  Min = cms.double( 70.0 ),
  Max = cms.double( -1.0 ),
  MinN = cms.int32( 1 )
)
process.hltHbhereco = cms.EDProducer( "HcalSimpleReconstructor",
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HBHE" ),
  firstSample = cms.int32( 4 ),
  samplesToAdd = cms.int32( 4 ),
  correctForTimeslew = cms.bool( True ),
  correctForPhaseContainment = cms.bool( True ),
  correctionPhaseNS = cms.double( 13.0 )
)
process.hltHcalCalibTypeFilter = cms.HLTFilter( "HLTHcalCalibTypeFilter",
  InputTag = cms.InputTag( "source" ),
  FilterSummary = cms.untracked.bool( False ),
  CalibTypes = cms.vint32( 1, 2, 3, 4, 5, 6 )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
  InputLabel = cms.InputTag( "source" ),
  HcalFirstFED = cms.untracked.int32( 0 ),
  UnpackCalib = cms.untracked.bool( True ),
  UnpackZDC = cms.untracked.bool( True ),
  UnpackTTP = cms.untracked.bool( False ),
  silent = cms.untracked.bool( True ),
  ComplainEmptyData = cms.untracked.bool( False ),
  ExpectedOrbitMessageTime = cms.untracked.int32( 0 ),
  FEDs = cms.untracked.vint32(  ),
  firstSample = cms.int32( 0 ),
  lastSample = cms.int32( 9 ),
  FilterDataQuality = cms.bool( True )
)
process.hltHcalMETNoiseFilter = cms.HLTFilter( "HLTHcalMETNoiseFilter",
  HcalNoiseRBXCollection = cms.InputTag( "hltHcalNoiseInfoProducer" ),
  severity = cms.int32( 1 ),
  maxNumRBXs = cms.int32( 2 ),
  numRBXsToConsider = cms.int32( 2 ),
  needEMFCoincidence = cms.bool( True ),
  minRBXEnergy = cms.double( 50.0 ),
  minRatio = cms.double( 0.65 ),
  maxRatio = cms.double( 0.98 ),
  minHPDHits = cms.int32( 17 ),
  minRBXHits = cms.int32( 999 ),
  minHPDNoOtherHits = cms.int32( 10 ),
  minZeros = cms.int32( 10 ),
  minHighEHitTime = cms.double( -9999.0 ),
  maxHighEHitTime = cms.double( 9999.0 ),
  maxRBXEMF = cms.double( 0.02 ),
  minRecHitE = cms.double( 1.5 ),
  minLowHitE = cms.double( 10.0 ),
  minHighHitE = cms.double( 25.0 )
)
process.hltHcalNoiseInfoProducer = cms.EDProducer( "HcalNoiseInfoProducer",
  pMinERatio = cms.double( 25.0 ),
  pMinEZeros = cms.double( 5.0 ),
  pMinEEMF = cms.double( 10.0 ),
  minERatio = cms.double( 50.0 ),
  minEZeros = cms.double( 10.0 ),
  minEEMF = cms.double( 50.0 ),
  pMinE = cms.double( 10.0 ),
  pMinRatio = cms.double( 0.75 ),
  pMaxRatio = cms.double( 0.85 ),
  pMinHPDHits = cms.int32( 10 ),
  pMinRBXHits = cms.int32( 20 ),
  pMinHPDNoOtherHits = cms.int32( 7 ),
  pMinZeros = cms.int32( 4 ),
  pMinLowEHitTime = cms.double( -6.0 ),
  pMaxLowEHitTime = cms.double( 6.0 ),
  pMinHighEHitTime = cms.double( -4.0 ),
  pMaxHighEHitTime = cms.double( 5.0 ),
  pMaxHPDEMF = cms.double( 0.02 ),
  pMaxRBXEMF = cms.double( 0.02 ),
  lMinRatio = cms.double( 0.7 ),
  lMaxRatio = cms.double( 0.96 ),
  lMinHPDHits = cms.int32( 17 ),
  lMinRBXHits = cms.int32( 999 ),
  lMinHPDNoOtherHits = cms.int32( 10 ),
  lMinZeros = cms.int32( 10 ),
  lMinLowEHitTime = cms.double( -9999.9 ),
  lMaxLowEHitTime = cms.double( 9999.0 ),
  lMinHighEHitTime = cms.double( -7.0 ),
  lMaxHighEHitTime = cms.double( 6.0 ),
  tMinRatio = cms.double( 0.73 ),
  tMaxRatio = cms.double( 0.92 ),
  tMinHPDHits = cms.int32( 16 ),
  tMinRBXHits = cms.int32( 50 ),
  tMinHPDNoOtherHits = cms.int32( 9 ),
  tMinZeros = cms.int32( 8 ),
  tMinLowEHitTime = cms.double( -9999.0 ),
  tMaxLowEHitTime = cms.double( 9999.0 ),
  tMinHighEHitTime = cms.double( -5.0 ),
  tMaxHighEHitTime = cms.double( 4.0 ),
  hlMaxHPDEMF = cms.double( -999.0 ),
  hlMaxRBXEMF = cms.double( 0.01 ),
  fillDigis = cms.bool( True ),
  fillRecHits = cms.bool( True ),
  fillCaloTowers = cms.bool( True ),
  fillTracks = cms.bool( False ),
  maxProblemRBXs = cms.int32( 20 ),
  maxCaloTowerIEta = cms.int32( 20 ),
  maxTrackEta = cms.double( 2.0 ),
  minTrackPt = cms.double( 1.0 ),
  digiCollName = cms.string( "hltHcalDigis" ),
  recHitCollName = cms.string( "hltHbhereco" ),
  caloTowerCollName = cms.string( "hltTowerMakerForAll" ),
  trackCollName = cms.string( "generalTracks" ),
  minRecHitE = cms.double( 1.5 ),
  minLowHitE = cms.double( 10.0 ),
  minHighHitE = cms.double( 25.0 ),
  HcalAcceptSeverityLevel = cms.uint32( 999 )
)
process.hltHcalTowerFilter = cms.HLTFilter( "HLTHcalTowerFilter",
  inputTag = cms.InputTag( "hltTowerMakerForHcal" ),
  saveTag = cms.untracked.bool( False ),
  MinE = cms.double( 5.0 ),
  MaxN = cms.int32( 20 )
)
process.hltHfreco = cms.EDProducer( "HcalSimpleReconstructor",
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HF" ),
  firstSample = cms.int32( 3 ),
  samplesToAdd = cms.int32( 4 ),
  correctForTimeslew = cms.bool( False ),
  correctForPhaseContainment = cms.bool( False ),
  correctionPhaseNS = cms.double( 0.0 )
)
process.hltHoreco = cms.EDProducer( "HcalSimpleReconstructor",
  digiLabel = cms.InputTag( "hltHcalDigis" ),
  dropZSmarkedPassed = cms.bool( True ),
  Subdetector = cms.string( "HO" ),
  firstSample = cms.int32( 4 ),
  samplesToAdd = cms.int32( 4 ),
  correctForTimeslew = cms.bool( True ),
  correctForPhaseContainment = cms.bool( True ),
  correctionPhaseNS = cms.double( 13.0 )
)
process.hltHybridSuperClustersActivity = cms.EDProducer( "HybridClusterProducer",
  debugLevel = cms.string( "ERROR" ),
  basicclusterCollection = cms.string( "hybridBarrelBasicClusters" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.string( "hltEcalRecHitAll" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0 = cms.double( 7.4 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  HybridBarrelSeedThr = cms.double( 1.0 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  clustershapecollection = cms.string( "" ),
  shapeAssociation = cms.string( "hybridShapeAssoc" ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltHybridSuperClustersL1Isolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( True ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0 = cms.double( 7.4 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  HybridBarrelSeedThr = cms.double( 1.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltHybridSuperClustersL1IsolatedLowPt = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( True ),
  l1LowerThr = cms.double( 3.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0 = cms.double( 7.4 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  HybridBarrelSeedThr = cms.double( 0.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltHybridSuperClustersL1NonIsolated = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( False ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0 = cms.double( 7.4 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  HybridBarrelSeedThr = cms.double( 1.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltHybridSuperClustersL1NonIsolatedLowPt = cms.EDProducer( "EgammaHLTHybridClusterProducer",
  debugLevel = cms.string( "INFO" ),
  basicclusterCollection = cms.string( "" ),
  superclusterCollection = cms.string( "" ),
  ecalhitproducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalhitcollection = cms.string( "EcalRecHitsEB" ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  doIsolated = cms.bool( False ),
  l1LowerThr = cms.double( 3.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.14 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0 = cms.double( 7.4 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  HybridBarrelSeedThr = cms.double( 0.5 ),
  step = cms.int32( 17 ),
  ethresh = cms.double( 0.1 ),
  eseed = cms.double( 0.35 ),
  ewing = cms.double( 0.0 ),
  dynamicEThresh = cms.bool( False ),
  eThreshA = cms.double( 0.003 ),
  eThreshB = cms.double( 0.1 ),
  severityRecHitThreshold = cms.double( 4.0 ),
  severitySpikeId = cms.int32( 2 ),
  severitySpikeThreshold = cms.double( 0.95 ),
  excludeFlagged = cms.bool( False ),
  dynamicPhiRoad = cms.bool( False ),
  RecHitFlagToBeExcluded = cms.vint32(  ),
  RecHitSeverityToBeExcluded = cms.vint32( 999 ),
  bremRecoveryPset = cms.PSet(

  )
)
process.hltIconeCentral1Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersCentral1Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeCentral2Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersCentral2Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeCentral3Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersCentral3Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeCentral4Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersCentral4Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeTau1Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersTau1Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeTau2Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersTau2Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeTau3Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersTau3Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIconeTau4Regional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.2 ),
  src = cms.InputTag( "hltCaloTowersTau4Regional" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIsolPixelTrackL2FilterHB8E29 = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltIsolPixelTrackProdHB8E29" ),
  MinPtTrack = cms.double( 3.5 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 1.3 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 8.0 ),
  NMaxTrackCandidates = cms.int32( 10 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL2FilterHE8E29 = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltIsolPixelTrackProdHE8E29" ),
  MinPtTrack = cms.double( 3.5 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 2.2 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 12.0 ),
  NMaxTrackCandidates = cms.int32( 5 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHB8E29 = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltHITIPTCorrectorHB8E29" ),
  MinPtTrack = cms.double( 20.0 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 1.3 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 38.0 ),
  NMaxTrackCandidates = cms.int32( 999 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackL3FilterHE8E29 = cms.HLTFilter( "HLTPixelIsolTrackFilter",
  candTag = cms.InputTag( "hltHITIPTCorrectorHE8E29" ),
  MinPtTrack = cms.double( 20.0 ),
  MaxPtNearby = cms.double( 2.0 ),
  MaxEtaTrack = cms.double( 2.2 ),
  MinEtaTrack = cms.double( 0.0 ),
  filterTrackEnergy = cms.bool( True ),
  MinEnergyTrack = cms.double( 38.0 ),
  NMaxTrackCandidates = cms.int32( 999 ),
  DropMultiL2Event = cms.bool( False )
)
process.hltIsolPixelTrackProdHB8E29 = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
  L1eTauJetsSource = cms.InputTag( "hltL1extraParticles:Tau" ),
  tauAssociationCone = cms.double( 0.0 ),
  tauUnbiasCone = cms.double( 0.0 ),
  ExtrapolationConeSize = cms.double( 1.0 ),
  PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
  L1GTSeedLabel = cms.InputTag( "hltL1sIsoTrackHB8E29" ),
  MaxVtxDXYSeed = cms.double( 101.0 ),
  MaxVtxDXYIsol = cms.double( 101.0 ),
  VertexLabel = cms.InputTag( "hltHITPixelVerticesHB" ),
  MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
  minPTrack = cms.double( 5.0 ),
  maxPTrackForIsolation = cms.double( 3.0 ),
  EBEtaBoundary = cms.double( 1.479 ),
  PixelTracksSources = cms.VInputTag( "hltHITPixelTracksHB" )
)
process.hltIsolPixelTrackProdHE8E29 = cms.EDProducer( "IsolatedPixelTrackCandidateProducer",
  L1eTauJetsSource = cms.InputTag( "hltL1extraParticles:Tau" ),
  tauAssociationCone = cms.double( 0.0 ),
  tauUnbiasCone = cms.double( 1.2 ),
  ExtrapolationConeSize = cms.double( 1.0 ),
  PixelIsolationConeSizeAtEC = cms.double( 40.0 ),
  L1GTSeedLabel = cms.InputTag( "hltL1sIsoTrackHE8E29" ),
  MaxVtxDXYSeed = cms.double( 101.0 ),
  MaxVtxDXYIsol = cms.double( 101.0 ),
  VertexLabel = cms.InputTag( "hltHITPixelVerticesHE" ),
  MagFieldRecordName = cms.string( "VolumeBasedMagneticField" ),
  minPTrack = cms.double( 5.0 ),
  maxPTrackForIsolation = cms.double( 3.0 ),
  EBEtaBoundary = cms.double( 1.479 ),
  PixelTracksSources = cms.VInputTag( "hltHITPixelTracksHB", "hltHITPixelTracksHE" )
)
process.hltIterativeCone5CaloJets = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.5 ),
  src = cms.InputTag( "hltTowerMakerForAll" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltIterativeCone5CaloJetsRegional = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.5 ),
  src = cms.InputTag( "hltTowerMakerForJets" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltJet20UEta3Ht = cms.EDProducer( "METProducer",
  src = cms.InputTag( "hltJetEta3Ht" ),
  InputType = cms.string( "CaloJetCollection" ),
  METType = cms.string( "MET" ),
  alias = cms.string( "HTMET" ),
  globalThreshold = cms.double( 20.0 ),
  noHF = cms.bool( False ),
  calculateSignificance = cms.bool( False ),
  onlyFiducialParticles = cms.bool( False ),
  usePt = cms.untracked.bool( False ),
  rf_type = cms.int32( 0 ),
  correctShowerTracks = cms.bool( False ),
  HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
  HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
  HB_PhiResPar = cms.vdouble( 0.02511 ),
  HE_PhiResPar = cms.vdouble( 0.02511 ),
  EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  EB_PhiResPar = cms.vdouble( 0.00502 ),
  EE_PhiResPar = cms.vdouble( 0.02511 ),
  HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
  EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  HF_PhiResPar = cms.vdouble( 0.05022 ),
  HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
  HO_PhiResPar = cms.vdouble( 0.02511 )
)
process.hltJet20UHt = cms.EDProducer( "METProducer",
  src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  InputType = cms.string( "CaloJetCollection" ),
  METType = cms.string( "MET" ),
  alias = cms.string( "HTMET" ),
  globalThreshold = cms.double( 20.0 ),
  noHF = cms.bool( False ),
  calculateSignificance = cms.bool( False ),
  onlyFiducialParticles = cms.bool( False ),
  usePt = cms.untracked.bool( False ),
  rf_type = cms.int32( 0 ),
  correctShowerTracks = cms.bool( False ),
  HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
  HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
  HB_PhiResPar = cms.vdouble( 0.02511 ),
  HE_PhiResPar = cms.vdouble( 0.02511 ),
  EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  EB_PhiResPar = cms.vdouble( 0.00502 ),
  EE_PhiResPar = cms.vdouble( 0.02511 ),
  HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
  EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  HF_PhiResPar = cms.vdouble( 0.05022 ),
  HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
  HO_PhiResPar = cms.vdouble( 0.02511 )
)
process.hltJetEta3Ht = cms.EDFilter( "CaloJetSelector",
  src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  filter = cms.bool( False ),
  cut = cms.string( "abs(eta)<3" )
)
process.hltL1EventNumberNZS = cms.HLTFilter( "HLTL1NumberFilter",
  rawInput = cms.InputTag( "source" ),
  period = cms.uint32( 4096 ),
  invert = cms.bool( False )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
  GmtInputTag = cms.InputTag( "hltGtDigis" ),
  GctInputTag = cms.InputTag( "hltGctDigis" ),
  CastorInputTag = cms.InputTag( "castorL1Digis" ),
  ProduceL1GtDaqRecord = cms.bool( False ),
  ProduceL1GtEvmRecord = cms.bool( False ),
  ProduceL1GtObjectMapRecord = cms.bool( True ),
  WritePsbL1GtDaqRecord = cms.bool( False ),
  ReadTechnicalTriggerRecords = cms.bool( True ),
  EmulateBxInEvent = cms.int32( 1 ),
  AlternativeNrBxBoardDaq = cms.uint32( 0 ),
  AlternativeNrBxBoardEvm = cms.uint32( 0 ),
  BstLengthBytes = cms.int32( -1 ),
  Verbosity = cms.untracked.int32( 0 ),
  TechnicalTriggersInputTags = cms.VInputTag( "simBscDigis" ),
  RecordLength = cms.vint32( 3, 0 )
)
process.hltL1HLTDoubleIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sDoubleIsoTau15Trk5" ),
  EtMin = cms.double( 15.0 )
)
process.hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sDoubleOneLegIsoTau15Trk5" ),
  EtMin = cms.double( 15.0 )
)
process.hltL1HLTSingleIsoTau20Trk15MET20JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauHighPtIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau20Trk15MET20" ),
  EtMin = cms.double( 20.0 )
)
process.hltL1HLTSingleIsoTau20Trk5MET20JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau20Trk5MET20" ),
  EtMin = cms.double( 20.0 )
)
process.hltL1HLTSingleIsoTau30L120or30Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau30L120or30Trk5" ),
  EtMin = cms.double( 30.0 )
)
process.hltL1HLTSingleIsoTau30Trk5MET20JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL3TauIsolationSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sSingleIsoTau30Trk5MET20" ),
  EtMin = cms.double( 30.0 )
)
process.hltL1IsoEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltEgammaRegionalCTFFinalFitWithMaterial" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL1IsoEgammaRegionalCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL1IsoEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1IsoEgammaRegionalPixelSeedGenerator" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL1IsoEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
  ptMin = cms.double( 1.5 ),
  vertexZ = cms.double( 0.0 ),
  originRadius = cms.double( 0.02 ),
  originHalfLength = cms.double( 15.0 ),
  deltaEtaRegion = cms.double( 0.3 ),
  deltaPhiRegion = cms.double( 0.3 ),
  candTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  candTagEle = cms.InputTag( "pixelMatchElectrons" ),
  UseZInVertex = cms.bool( False ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  OrderedHitsFactoryPSet = cms.PSet(
    maxElement = cms.uint32( 0 ),
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerPairs" )
  )
)
process.hltL1IsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
  electronProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  trackProducer = cms.InputTag( "hltL1IsoEgammaRegionalCTFFinalFitWithMaterial" ),
  egTrkIsoPtMin = cms.double( 1.0 ),
  egTrkIsoConeSize = cms.double( 0.3 ),
  egTrkIsoZSpan = cms.double( 0.15 ),
  egTrkIsoRSpan = cms.double( 999999.0 ),
  egTrkIsoVetoConeSize = cms.double( 0.03 ),
  egCheckForOtherEleInCone = cms.untracked.bool( False ),
  egTrkIsoStripBarrel = cms.double( 0.03 ),
  egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1IsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  isIeta = cms.bool( True )
)
process.hltL1IsoHLTClusterShapeLowPt = cms.EDProducer( "EgammaHLTClusterShapeProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  isIeta = cms.bool( True )
)
process.hltL1IsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1IsoR9shapeLowPt = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1IsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1IsoRecoEcalCandidateLowPt = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1IsolatedLowPt" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1IsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1Isolated" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.15 ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 ),
      maxElement = cms.uint32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 3.0 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.2 ),
    rMinI = cms.double( -0.2 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.15 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.09 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.09 ),
    hbheInstance = cms.string( "" ),
    PhiMax2 = cms.double( 0.004 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    measurementTrackerName = cms.string( "hltMeasurementTracker" )
  )
)
process.hltL1IsoStartUpElectronPixelSeedsLowPt = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1IsolatedLowPt" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.08 ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 ),
      maxElement = cms.uint32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 0.3 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.11 ),
    rMinI = cms.double( -0.11 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.08 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.05 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.05 ),
    hbheInstance = cms.string( "" ),
    PhiMax2 = cms.double( 0.004 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    measurementTrackerName = cms.string( "hltMeasurementTracker" )
  )
)
process.hltL1IsolatedElectronHcalIsolLowPt = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.0 ),
  eMinHE = cms.double( 0.0 ),
  etMinHB = cms.double( 0.0 ),
  etMinHE = cms.double( 0.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.15 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( True )
)
process.hltL1IsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
  ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
  etMinBarrel = cms.double( -9999.0 ),
  eMinBarrel = cms.double( 0.08 ),
  etMinEndcap = cms.double( 0.1 ),
  eMinEndcap = cms.double( -9999.0 ),
  intRadiusBarrel = cms.double( 3.0 ),
  intRadiusEndcap = cms.double( 3.0 ),
  extRadius = cms.double( 0.3 ),
  jurassicWidth = cms.double( 3.0 ),
  useIsolEt = cms.bool( True ),
  tryBoth = cms.bool( True ),
  subtract = cms.bool( False ),
  useNumCrystals = cms.bool( True )
)
process.hltL1IsolatedPhotonEcalIsolLowPt = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
  ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
  etMinBarrel = cms.double( -9999.0 ),
  eMinBarrel = cms.double( 0.08 ),
  etMinEndcap = cms.double( -9999.0 ),
  eMinEndcap = cms.double( 0.3 ),
  intRadiusBarrel = cms.double( 0.045 ),
  intRadiusEndcap = cms.double( 0.07 ),
  extRadius = cms.double( 0.4 ),
  jurassicWidth = cms.double( 0.02 ),
  useIsolEt = cms.bool( True ),
  tryBoth = cms.bool( True ),
  subtract = cms.bool( False ),
  useNumCrystals = cms.bool( False )
)
process.hltL1IsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.14 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( False )
)
process.hltL1IsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.16 ),
  outerCone = cms.double( 0.29 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( True )
)
process.hltL1IsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  trackProducer = cms.InputTag( "hltL1IsoEgammaRegionalCTFFinalFitWithMaterial" ),
  countTracks = cms.bool( False ),
  egTrkIsoPtMin = cms.double( 1.0 ),
  egTrkIsoConeSize = cms.double( 0.29 ),
  egTrkIsoZSpan = cms.double( 999999.0 ),
  egTrkIsoRSpan = cms.double( 999999.0 ),
  egTrkIsoVetoConeSize = cms.double( 0.06 ),
  egTrkIsoStripBarrel = cms.double( 0.03 ),
  egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch = cms.EDProducer( "L1HLTJetsMatching",
  JetSrc = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  L1TauTrigger = cms.InputTag( "hltL1sDoubleOneLegIsoTau15Trk5" ),
  EtMin = cms.double( 15.0 )
)
process.hltL1Mu20L1Filtered20 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu20" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 20.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1Mu3Jet10UL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1Mu3Jet10U" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1Mu7L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu7" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenL1SingleMu0" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1MuOpenL1FilteredDT = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenL1SingleMu0" ),
  MaxEta = cms.double( 1.25 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltL1NonIsoDoublePhotonEt4eeResClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt4eeResR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShapeLowPt" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShapeLowPt" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.016 ),
  thrRegularEE = cms.double( 0.042 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoDoublePhotonEt4eeResEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsolLowPt" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsolLowPt" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoDoublePhotonEt4eeResEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResL1MatchFilterRegional" ),
  etcutEB = cms.double( 4.0 ),
  etcutEE = cms.double( 4.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoDoublePhotonEt4eeResHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedElectronHcalIsolLowPt" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedElectronHcalIsolLowPt" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.17 ),
  thrOverEEE = cms.double( 0.18 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoDoublePhotonEt4eeResL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG2" ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoDoublePhotonEt4eeResOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchStartUpWindowElectronsL1IsoLowPt" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchStartUpWindowElectronsL1NonIsoLowPt" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True )
)
process.hltL1NonIsoDoublePhotonEt4eeResPMMassFilter = cms.HLTFilter( "HLTPMMassFilter",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResOneOEMinusOneOPFilter" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  lowerMassCut = cms.double( 2.0 ),
  upperMassCut = cms.double( 15.0 ),
  nZcandcut = cms.int32( 1 ),
  reqOppCharge = cms.untracked.bool( False ),
  isElectron1 = cms.untracked.bool( True ),
  isElectron2 = cms.untracked.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchStartUpWindowElectronsL1IsoLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchStartUpWindowElectronsL1NonIsoLowPt" )
)
process.hltL1NonIsoDoublePhotonEt4eeResPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResHcalIsolFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeedsLowPt" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeedsLowPt" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltEgammaRegionalCTFFinalFitWithMaterial" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL1NonIsoEgammaRegionalCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL1NonIsoEgammaRegionalCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL1NonIsoEgammaRegionalPixelSeedGenerator" ),
  TrajectoryBuilder = cms.string( "hltCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL1NonIsoEgammaRegionalPixelSeedGenerator = cms.EDProducer( "EgammaHLTRegionalPixelSeedGeneratorProducers",
  ptMin = cms.double( 1.5 ),
  vertexZ = cms.double( 0.0 ),
  originRadius = cms.double( 0.02 ),
  originHalfLength = cms.double( 15.0 ),
  deltaEtaRegion = cms.double( 0.3 ),
  deltaPhiRegion = cms.double( 0.3 ),
  candTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  candTagEle = cms.InputTag( "pixelMatchElectrons" ),
  UseZInVertex = cms.bool( False ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  OrderedHitsFactoryPSet = cms.PSet(
    maxElement = cms.uint32( 0 ),
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerPairs" )
  )
)
process.hltL1NonIsoElectronTrackIsol = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
  electronProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  trackProducer = cms.InputTag( "hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial" ),
  egTrkIsoPtMin = cms.double( 1.0 ),
  egTrkIsoConeSize = cms.double( 0.3 ),
  egTrkIsoZSpan = cms.double( 0.15 ),
  egTrkIsoRSpan = cms.double( 999999.0 ),
  egTrkIsoVetoConeSize = cms.double( 0.03 ),
  egCheckForOtherEleInCone = cms.untracked.bool( False ),
  egTrkIsoStripBarrel = cms.double( 0.03 ),
  egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1NonIsoHLTClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  isIeta = cms.bool( True )
)
process.hltL1NonIsoHLTClusterShapeLowPt = cms.EDProducer( "EgammaHLTClusterShapeProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  isIeta = cms.bool( True )
)
process.hltL1NonIsoHLTNonIsoDoubleElectronEt15EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt15L1MatchFilterRegional" ),
  etcutEB = cms.double( 15.0 ),
  etcutEE = cms.double( 15.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoDoubleElectronEt15HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt15EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.0 ),
  thrRegularEE = cms.double( 0.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoDoubleElectronEt15L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoDoubleElectronEt15PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoubleElectronEt15HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoDoublePhotonEt17EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17L1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoDoublePhotonEt17HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoDoublePhotonEt17EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoDoublePhotonEt17L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1DoubleEG5" ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoDoublePhotonEt4eeResR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoDoublePhotonEt4eeResEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shapeLowPt" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shapeLowPt" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidateLowPt" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" )
)
process.hltL1NonIsoHLTNonIsoSingleEle10MET45EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 10.0 ),
  etcutEE = cms.double( 10.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleEle10MET45HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleEle10MET45R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActvityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleEle10MET45PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleEle10MET45HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleEle10MET45R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleEle10MET45EtFilter" ),
  isoTag = cms.InputTag( "hltActivityR9shape" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional" ),
  etcutEB = cms.double( 10.0 ),
  etcutEE = cms.double( 10.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG5" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt10PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdL1MatchFilterRegional" ),
  etcutEB = cms.double( 12.0 ),
  etcutEE = cms.double( 12.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.125 ),
  thrOverEEE = cms.double( 0.075 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.011 ),
  thrRegularEE = cms.double( 0.031 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional" ),
  etcutEB = cms.double( 12.0 ),
  etcutEE = cms.double( 12.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.011 ),
  thrRegularEE = cms.double( 0.031 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional" ),
  etcutEB = cms.double( 12.0 ),
  etcutEE = cms.double( 12.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( 999999.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter" ),
  isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverPtEB = cms.double( 0.15 ),
  thrOverPtEE = cms.double( 0.1 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  useEt = cms.untracked.bool( True )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TIghtEleIdIsolDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.125 ),
  thrOverEEE = cms.double( 0.075 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 8.0 ),
  etcutEE = cms.double( 8.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoublePixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter" ),
  isoTag = cms.InputTag( "hltActivityR9Shape" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HER9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 8.0 ),
  etcutEE = cms.double( 8.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleEtFilter" ),
  isoTag = cms.InputTag( "hltActivityR9Shape" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HER9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.125 ),
  thrOverEEE = cms.double( 0.075 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( 999999.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHcalIsolFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolTrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TIghtEleIdIsolDphiFilter" ),
  isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverPtEB = cms.double( 0.15 ),
  thrOverPtEE = cms.double( 0.1 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.011 ),
  thrRegularEE = cms.double( 0.031 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.011 ),
  thrRegularEE = cms.double( 0.031 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.01 ),
  thrRegularEE = cms.double( 0.01 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 0.08 ),
  thrRegularEE = cms.double( 0.08 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( 999999.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolTrackIsolFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter" ),
  isoTag = cms.InputTag( "hltL1IsoElectronTrackIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoElectronTrackIsol" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverPtEB = cms.double( 0.15 ),
  thrOverPtEE = cms.double( 0.1 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  useEt = cms.untracked.bool( True )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27CaloEleIdTrackDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 99999.9 ),
  thrRegularEE = cms.double( 99999.9 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 99999.9 ),
  thrRegularEE = cms.double( 99999.9 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackL1MatchFilterRegional" ),
  etcutEB = cms.double( 27.0 ),
  etcutEE = cms.double( 27.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32CaloEleIdTrackDphiFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackDetaFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Dphi" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Dphi" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 99999.9 ),
  thrRegularEE = cms.double( 99999.9 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackClusterShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoHLTClusterShape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoHLTClusterShape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.012 ),
  thrRegularEE = cms.double( 0.032 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackDetaFilter = cms.HLTFilter( "HLTElectronGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackOneOEMinusOneOPFilter" ),
  isoTag = cms.InputTag( "hltElectronL1IsoDetaDphi:Deta" ),
  nonIsoTag = cms.InputTag( "hltElectronL1NonIsoDetaDphi:Deta" ),
  lessThan = cms.bool( True ),
  thrRegularEB = cms.double( 99999.9 ),
  thrRegularEE = cms.double( 99999.9 ),
  thrOverPtEB = cms.double( -1.0 ),
  thrOverPtEE = cms.double( -1.0 ),
  thrTimesPtEB = cms.double( -1.0 ),
  thrTimesPtEE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  L1NonIsoCand = cms.InputTag( "hltPixelMatchElectronsL1NonIso" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackL1MatchFilterRegional" ),
  etcutEB = cms.double( 32.0 ),
  etcutEE = cms.double( 32.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackClusterShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.1 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackOneOEMinusOneOPFilter = cms.HLTFilter( "HLTElectronOneOEMinusOneOPFilterRegional",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackPixelMatchFilter" ),
  electronIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1Iso" ),
  electronNonIsolatedProducer = cms.InputTag( "hltPixelMatchElectronsL1NonIso" ),
  barrelcut = cms.double( 999.9 ),
  endcapcut = cms.double( 999.9 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackPixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackHEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele5EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 5.0 ),
  etcutEE = cms.double( 5.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele5HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele5R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele5PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele5HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltActivityStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele5R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele5EtFilter" ),
  isoTag = cms.InputTag( "hltActivityR9shape" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele9EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele9L1MatchFilterRegional" ),
  etcutEB = cms.double( 9.0 ),
  etcutEE = cms.double( 9.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele9HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele9R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele9L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1Mu3EG5" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele9PixelMatchFilter = cms.HLTFilter( "HLTElectronPixelMatchFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele9HEFilter" ),
  L1IsoPixelSeedsTag = cms.InputTag( "hltL1IsoStartUpElectronPixelSeeds" ),
  L1NonIsoPixelSeedsTag = cms.InputTag( "hltL1NonIsoStartUpElectronPixelSeeds" ),
  npixelmatchcut = cms.double( 1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSingleMu5Ele9R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSingleMu5Ele9EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 100.0 ),
  etcutEE = cms.double( 100.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional" ),
  etcutEB = cms.double( 10.0 ),
  etcutEE = cms.double( 10.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt10HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG5" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 11.0 ),
  etcutEE = cms.double( 11.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1Mu3EG5" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 15.0 ),
  etcutEE = cms.double( 15.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltEcalActivitySuperClusterWrapper" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 2 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltActivityPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleEtFilter" ),
  isoTag = cms.InputTag( "hltActivityR9Shape" ),
  nonIsoTag = cms.InputTag( "" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 2 ),
  doIsolated = cms.bool( True ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltRecoEcalSuperClusterActivityCandidate" ),
  L1NonIsoCand = cms.InputTag( "" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEL1MatchFilterRegional" ),
  etcutEB = cms.double( 17.0 ),
  etcutEE = cms.double( 17.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HER9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HER9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 20.0 ),
  etcutEE = cms.double( 20.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional" ),
  etcutEB = cms.double( 20.0 ),
  etcutEE = cms.double( 20.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 30.0 ),
  etcutEE = cms.double( 30.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 30.0 ),
  etcutEE = cms.double( 999999.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedTrackIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonEcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonEcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 35.0 ),
  etcutEE = cms.double( 35.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEcalIsolFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.05 ),
  thrOverEEE = cms.double( 0.05 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHcalIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedTrackIsolFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHEFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHollowTrackIsol" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHollowTrackIsol" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( True ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.2 ),
  thrOverEEE = cms.double( 0.1 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 50.0 ),
  etcutEE = cms.double( 50.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( -1.0 ),
  thrRegularEE = cms.double( -1.0 ),
  thrOverEEB = cms.double( 0.15 ),
  thrOverEEE = cms.double( 0.15 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional" ),
  etcutEB = cms.double( 50.0 ),
  etcutEE = cms.double( 50.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50HEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedEtFilter = cms.HLTFilter( "HLTEgammaEtFilter",
  inputTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedL1MatchFilterRegional" ),
  etcutEB = cms.double( 70.0 ),
  etcutEE = cms.double( 70.0 ),
  ncandcut = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  relaxed = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedHEFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedR9ShapeFilter" ),
  isoTag = cms.InputTag( "hltL1IsolatedPhotonHcalForHE" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsolatedPhotonHcalForHE" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 999999.9 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( True ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedL1MatchFilterRegional = cms.HLTFilter( "HLTEgammaL1MatchFilterRegional",
  candIsolatedTag = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  l1IsolatedTag = cms.InputTag( "hltL1extraParticles:Isolated" ),
  candNonIsolatedTag = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  l1NonIsolatedTag = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG8" ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  region_eta_size = cms.double( 0.522 ),
  region_eta_size_ecap = cms.double( 1.0 ),
  region_phi_size = cms.double( 1.044 ),
  barrel_end = cms.double( 1.4791 ),
  endcap_end = cms.double( 2.65 )
)
process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedR9ShapeFilter = cms.HLTFilter( "HLTEgammaGenericFilter",
  candTag = cms.InputTag( "hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedEtFilter" ),
  isoTag = cms.InputTag( "hltL1IsoR9shape" ),
  nonIsoTag = cms.InputTag( "hltL1NonIsoR9shape" ),
  lessThan = cms.bool( True ),
  useEt = cms.bool( False ),
  thrRegularEB = cms.double( 0.98 ),
  thrRegularEE = cms.double( 999999.9 ),
  thrOverEEB = cms.double( -1.0 ),
  thrOverEEE = cms.double( -1.0 ),
  thrOverE2EB = cms.double( -1.0 ),
  thrOverE2EE = cms.double( -1.0 ),
  ncandcut = cms.int32( 1 ),
  doIsolated = cms.bool( False ),
  SaveTag = cms.untracked.bool( False ),
  L1IsoCand = cms.InputTag( "hltL1IsoRecoEcalCandidate" ),
  L1NonIsoCand = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" )
)
process.hltL1NonIsoR9shape = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHit:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1NonIsoR9shapeLowPt = cms.EDProducer( "EgammaHLTR9Producer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" ),
  ecalRechitEB = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEB" ),
  ecalRechitEE = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt:EcalRecHitsEE" ),
  useSwissCross = cms.bool( False )
)
process.hltL1NonIsoRecoEcalCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1NonIsoRecoEcalCandidateLowPt = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedLowPt" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltL1NonIsoStartUpElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolated" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.15 ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 ),
      maxElement = cms.uint32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 3.0 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.2 ),
    rMinI = cms.double( -0.2 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.15 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.09 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.09 ),
    hbheInstance = cms.string( "" ),
    PhiMax2 = cms.double( 0.004 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    measurementTrackerName = cms.string( "hltMeasurementTracker" )
  )
)
process.hltL1NonIsoStartUpElectronPixelSeedsLowPt = cms.EDProducer( "ElectronSeedProducer",
  barrelSuperClusters = cms.InputTag( "hltCorrectedHybridSuperClustersL1NonIsolatedLowPt" ),
  endcapSuperClusters = cms.InputTag( "hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NoIsolatedLowPt" ),
  SeedConfiguration = cms.PSet(
    searchInTIDTEC = cms.bool( True ),
    HighPtThreshold = cms.double( 35.0 ),
    r2MinF = cms.double( -0.08 ),
    OrderedHitsFactoryPSet = cms.PSet(
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      SeedingLayers = cms.string( "hltMixedLayerPairs" ),
      useOnDemandTracker = cms.untracked.int32( 0 ),
      maxElement = cms.uint32( 0 )
    ),
    DeltaPhi1Low = cms.double( 0.23 ),
    DeltaPhi1High = cms.double( 0.08 ),
    ePhiMin1 = cms.double( -0.08 ),
    PhiMin2 = cms.double( -0.004 ),
    LowPtThreshold = cms.double( 0.1 ),
    RegionPSet = cms.PSet(
      deltaPhiRegion = cms.double( 0.4 ),
      originHalfLength = cms.double( 15.0 ),
      useZInVertex = cms.bool( True ),
      deltaEtaRegion = cms.double( 0.1 ),
      ptMin = cms.double( 1.5 ),
      originRadius = cms.double( 0.2 ),
      VertexProducer = cms.InputTag( "dummyVertices" )
    ),
    maxHOverE = cms.double( 999999.0 ),
    dynamicPhiRoad = cms.bool( False ),
    ePhiMax1 = cms.double( 0.04 ),
    DeltaPhi2 = cms.double( 0.004 ),
    SizeWindowENeg = cms.double( 0.675 ),
    nSigmasDeltaZ1 = cms.double( 5.0 ),
    rMaxI = cms.double( 0.11 ),
    rMinI = cms.double( -0.11 ),
    preFilteredSeeds = cms.bool( True ),
    r2MaxF = cms.double( 0.08 ),
    pPhiMin1 = cms.double( -0.04 ),
    initialSeeds = cms.InputTag( "noSeedsHere" ),
    pPhiMax1 = cms.double( 0.08 ),
    hbheModule = cms.string( "hbhereco" ),
    SCEtCut = cms.double( 3.0 ),
    z2MaxB = cms.double( 0.05 ),
    fromTrackerSeeds = cms.bool( True ),
    hcalRecHits = cms.InputTag( "hltHbhereco" ),
    z2MinB = cms.double( -0.05 ),
    hbheInstance = cms.string( "" ),
    PhiMax2 = cms.double( 0.004 ),
    hOverEConeSize = cms.double( 0.0 ),
    hOverEHBMinE = cms.double( 999999.0 ),
    applyHOverECut = cms.bool( False ),
    hOverEHFMinE = cms.double( 999999.0 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    measurementTrackerName = cms.string( "hltMeasurementTracker" )
  )
)
process.hltL1NonIsolatedElectronHcalIsolLowPt = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.0 ),
  eMinHE = cms.double( 0.0 ),
  etMinHB = cms.double( 0.0 ),
  etMinHE = cms.double( 0.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.15 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( True )
)
process.hltL1NonIsolatedPhotonEcalIsol = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
  ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
  etMinBarrel = cms.double( -9999.0 ),
  eMinBarrel = cms.double( 0.08 ),
  etMinEndcap = cms.double( 0.1 ),
  eMinEndcap = cms.double( -9999.0 ),
  intRadiusBarrel = cms.double( 3.0 ),
  intRadiusEndcap = cms.double( 3.0 ),
  extRadius = cms.double( 0.3 ),
  jurassicWidth = cms.double( 3.0 ),
  useIsolEt = cms.bool( True ),
  tryBoth = cms.bool( True ),
  subtract = cms.bool( False ),
  useNumCrystals = cms.bool( True )
)
process.hltL1NonIsolatedPhotonEcalIsolLowPt = cms.EDProducer( "EgammaHLTEcalRecIsolationProducer",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidateLowPt" ),
  ecalBarrelRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalBarrelRecHitCollection = cms.InputTag( "EcalRecHitsEB" ),
  ecalEndcapRecHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  ecalEndcapRecHitCollection = cms.InputTag( "EcalRecHitsEE" ),
  etMinBarrel = cms.double( -9999.0 ),
  eMinBarrel = cms.double( 0.08 ),
  etMinEndcap = cms.double( -9999.0 ),
  eMinEndcap = cms.double( 0.3 ),
  intRadiusBarrel = cms.double( 0.045 ),
  intRadiusEndcap = cms.double( 0.07 ),
  extRadius = cms.double( 0.4 ),
  jurassicWidth = cms.double( 0.02 ),
  useIsolEt = cms.bool( True ),
  tryBoth = cms.bool( True ),
  subtract = cms.bool( False ),
  useNumCrystals = cms.bool( False )
)
process.hltL1NonIsolatedPhotonHcalForHE = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.0 ),
  outerCone = cms.double( 0.14 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( False )
)
process.hltL1NonIsolatedPhotonHcalIsol = cms.EDProducer( "EgammaHLTHcalIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  hbheRecHitProducer = cms.InputTag( "hltHbhereco" ),
  eMinHB = cms.double( 0.7 ),
  eMinHE = cms.double( 0.8 ),
  etMinHB = cms.double( -1.0 ),
  etMinHE = cms.double( -1.0 ),
  innerCone = cms.double( 0.16 ),
  outerCone = cms.double( 0.29 ),
  depth = cms.int32( -1 ),
  doEtSum = cms.bool( True )
)
process.hltL1NonIsolatedPhotonHollowTrackIsol = cms.EDProducer( "EgammaHLTPhotonTrackIsolationProducersRegional",
  recoEcalCandidateProducer = cms.InputTag( "hltL1NonIsoRecoEcalCandidate" ),
  trackProducer = cms.InputTag( "hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial" ),
  countTracks = cms.bool( False ),
  egTrkIsoPtMin = cms.double( 1.0 ),
  egTrkIsoConeSize = cms.double( 0.29 ),
  egTrkIsoZSpan = cms.double( 999999.0 ),
  egTrkIsoRSpan = cms.double( 999999.0 ),
  egTrkIsoVetoConeSize = cms.double( 0.06 ),
  egTrkIsoStripBarrel = cms.double( 0.03 ),
  egTrkIsoStripEndcap = cms.double( 0.03 )
)
process.hltL1SingleMu0L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu3EG5L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1Mu3EG5" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu3L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu5L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu5" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1SingleMu7L1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu7" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltL1TechBSChalo = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "L1Tech_BSC_halo_beam2_inner", "L1Tech_BSC_halo_beam2_outer", "L1Tech_BSC_halo_beam1_inner", "L1Tech_BSC_halo_beam1_outer" ),
  hltResults = cms.InputTag( "" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltL1TechBSCminBias = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "L1Tech_BSC_minBias_inner_threshold1", "L1Tech_BSC_minBias_inner_threshold2", "L1Tech_BSC_minBias_threshold1", "L1Tech_BSC_minBias_threshold2" ),
  hltResults = cms.InputTag( "" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltL1TechBSCminBiasOR = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "L1Tech_BSC_minBias_OR" ),
  hltResults = cms.InputTag( "" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltL1TechHCALHF = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "L1Tech_HCAL_HF_MM_or_PP_or_PM", "L1Tech_HCAL_HF_coincidence_PM", "L1Tech_HCAL_HF_MMP_or_MPP" ),
  hltResults = cms.InputTag( "" ),
  l1tResults = cms.InputTag( "hltGtDigis" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
  produceMuonParticles = cms.bool( True ),
  muonSource = cms.InputTag( "hltGtDigis" ),
  produceCaloParticles = cms.bool( True ),
  isolatedEmSource = cms.InputTag( "hltGctDigis:isoEm" ),
  nonIsolatedEmSource = cms.InputTag( "hltGctDigis:nonIsoEm" ),
  centralJetSource = cms.InputTag( "hltGctDigis:cenJets" ),
  forwardJetSource = cms.InputTag( "hltGctDigis:forJets" ),
  tauJetSource = cms.InputTag( "hltGctDigis:tauJets" ),
  etTotalSource = cms.InputTag( "hltGctDigis" ),
  etHadSource = cms.InputTag( "hltGctDigis" ),
  etMissSource = cms.InputTag( "hltGctDigis" ),
  htMissSource = cms.InputTag( "hltGctDigis" ),
  hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
  hfRingBitCountsSource = cms.InputTag( "hltGctDigis" ),
  centralBxOnly = cms.bool( True ),
  ignoreHtMiss = cms.bool( False )
)
process.hltL1sAlCaEcalPi0Eta8E29 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleIsoEG5 OR L1_SingleIsoEG8 OR L1_SingleIsoEG10 OR L1_SingleIsoEG12 OR L1_SingleIsoEG15 OR L1_SingleEG2 OR L1_SingleEG5 OR L1_SingleEG8 OR L1_SingleEG10 OR L1_SingleEG12 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleJet6U OR L1_SingleJet10U OR L1_SingleJet20U OR L1_SingleJet30U OR L1_SingleJet40U OR L1_SingleJet50U OR L1_DoubleJet30U OR L1_DoubleEG2 OR L1_DoubleEG5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sAlCaRPC = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen OR L1_SingleMu0 OR L1_SingleMu3 OR L1_SingleMu7" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sBTagMuDiJet10U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet6U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sDoubleIsoTau15Trk5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet14U OR L1_DoubleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleTauJet14U OR L1_DoubleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sETT60 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT60" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sGlobalRunHPDNoise = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U_NotBptxOR" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sHcalNZS8E29 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG2 OR L1_SingleEG5 OR L1_SingleEG8 OR L1_SingleEG10 OR L1_SingleEG12 OR L1_SingleEG15 OR L1_SingleEG20 OR L1_SingleIsoEG5 OR L1_SingleIsoEG8 OR L1_SingleIsoEG10 OR L1_SingleIsoEG12 OR L1_SingleIsoEG15 OR L1_SingleJet6U OR L1_SingleJet10U OR L1_SingleJet20U OR L1_SingleJet30U OR L1_SingleJet40U OR L1_SingleJet50U OR L1_SingleJet60U OR L1_SingleTauJet10U OR L1_SingleTauJet20U OR L1_SingleTauJet30U OR L1_SingleTauJet50U OR L1_SingleMuOpen OR L1_SingleMu0 OR L1_SingleMu3 OR L1_SingleMu5 OR L1_SingleMu7 OR L1_SingleMu10 OR L1_SingleMu14 OR L1_SingleMu20 OR L1_ZeroBias" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sHighMultiplicityBSC = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "35" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sIsoTrackHB8E29 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sIsoTrackHE8E29 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet20U OR L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sJet30U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet20U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sJet50U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BPTX = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "3" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BPTXMinusOnly = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BptxMinus_NotBptxPlus" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BPTXPlusOnly = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BptxPlus_NotBptxMinus" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BptxXORBscMinBiasOR = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BptxXOR_BscMinBiasOR" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1BscMinBiasORBptxPlusANDMinus = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_BscMinBiasOR_BptxPlusANDMinus" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleEG2 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleEG2" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleEG5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleEG5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleForJet10UEtaOpp = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleForJet10U_EtaOpp" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1DoubleMuOpen = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_DoubleMuOpen" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETM20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETM20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETM30 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETM30" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETT100 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT100" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1ETT140 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETT140" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1HTT50 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_HTT50" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Jet10U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Jet6U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet6U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1MET20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_ETM20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu3EG5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_Mu3_EG5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1Mu3Jet10U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_Mu3_Jet10U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1QuadJet8U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_QuadJet8U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG2 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG2" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleEG8 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleEG8" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet10U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet10UNotBptxOR = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet10U_NotBptxOR" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( False )
)
process.hltL1sL1SingleJet20U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet20U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet30U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet40U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet40U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet60U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet60U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleJet6U = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleJet6U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu0 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu0" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu20" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu3 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu3" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu5" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMu7 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMu7" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpenL1SingleMu0 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen OR L1_SingleMu0" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleMuOpen OR L1_SingleMu0 OR L1_SingleMu3" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sL1TechRPCTTURBst1collisions = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "31" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sNotBptxPlusOrMinus = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "NOT L1_BptxPlusORMinus" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sRPCBarrelCosmics = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "24" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( False ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "L1_SingleTauJet20U OR L1_SingleJet30U" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sTechTrigHCALNoise = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "11 OR 12" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sTrackerCosmics = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "25" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1sZeroBias = cms.HLTFilter( "HLTLevel1GTSeed",
  L1UseL1TriggerObjectMaps = cms.bool( True ),
  L1NrBxInEvent = cms.int32( 3 ),
  L1TechTriggerSeeding = cms.bool( True ),
  L1UseAliasesForSeeding = cms.bool( True ),
  L1SeedsLogicalExpression = cms.string( "4" ),
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
  L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
  L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
  saveTags = cms.untracked.bool( True )
)
process.hltL1tfed = cms.EDAnalyzer( "L1TFED",
  verbose = cms.untracked.bool( False ),
  rawTag = cms.InputTag( "source" ),
  DQMStore = cms.untracked.bool( True ),
  outputFile = cms.untracked.string( "" ),
  disableROOToutput = cms.untracked.bool( True ),
  FEDDirName = cms.untracked.string( "L1T/FEDIntegrity" ),
  stableROConfig = cms.untracked.bool( True ),
  L1FEDS = cms.vint32( 745, 760, 780, 812, 813 )
)
process.hltL25TauCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL25TauPixelSeeds" ),
  TrajectoryBuilder = cms.string( "trajBuilderL3" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL25TauConeIsolation = cms.EDProducer( "ConeIsolation",
  JetTrackSrc = cms.InputTag( "hltL25TauJetTracksAssociator" ),
  vertexSrc = cms.InputTag( "hltPixelVertices" ),
  useVertex = cms.bool( True ),
  useBeamSpot = cms.bool( True ),
  BeamSpotProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  MinimumNumberOfPixelHits = cms.int32( 2 ),
  MinimumNumberOfHits = cms.int32( 5 ),
  MaximumTransverseImpactParameter = cms.double( 300.0 ),
  MinimumTransverseMomentum = cms.double( 1.0 ),
  MaximumChiSquared = cms.double( 100.0 ),
  DeltaZetTrackVertex = cms.double( 0.2 ),
  MatchingCone = cms.double( 0.2 ),
  SignalCone = cms.double( 0.15 ),
  IsolationCone = cms.double( 0.5 ),
  MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
  UseFixedSizeCone = cms.bool( True ),
  VariableConeParameter = cms.double( 3.5 ),
  VariableMaxCone = cms.double( 0.17 ),
  VariableMinCone = cms.double( 0.05 )
)
process.hltL25TauCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracks" ),
  Fitter = cms.string( "FittingSmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltL25TauCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL25TauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
  jets = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
  tracks = cms.InputTag( "hltL25TauCtfWithMaterialTracks" ),
  coneSize = cms.double( 0.5 )
)
process.hltL25TauLeadingTrackHighPtCutSelector = cms.EDProducer( "IsolatedTauJetsSelector",
  MinimumTransverseMomentumLeadingTrack = cms.double( 15.0 ),
  UseIsolationDiscriminator = cms.bool( False ),
  UseInHLTOpen = cms.bool( False ),
  JetSrc = cms.VInputTag( "hltL25TauConeIsolation" )
)
process.hltL25TauLeadingTrackPtCutSelector = cms.EDProducer( "IsolatedTauJetsSelector",
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  UseIsolationDiscriminator = cms.bool( False ),
  UseInHLTOpen = cms.bool( False ),
  JetSrc = cms.VInputTag( "hltL25TauConeIsolation" )
)
process.hltL25TauPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      deltaPhiRegion = cms.double( 0.2 ),
      originHalfLength = cms.double( 0.2 ),
      originRadius = cms.double( 0.2 ),
      deltaEtaRegion = cms.double( 0.2 ),
      vertexSrc = cms.InputTag( "hltPixelVertices" ),
      JetSrc = cms.InputTag( "hltL2TauRelaxingIsolationSelector:Isolated" ),
      originZPos = cms.double( 0.0 ),
      ptMin = cms.double( 4.0 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerPairs" ),
    maxElement = cms.uint32( 0 )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltL2DoubleMu20NoVertexL2PreFiltered = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 2 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 20.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu30L2Filtered30 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 30.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltL2Mu5Jet10UL2Filtered4 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1Mu3Jet10UL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 4.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltL2Mu7L2Filtered7 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 7.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL2Muons:UpdatedAtVtx" )
)
process.hltL2MuonCandidatesNoVtx = cms.EDProducer( "L2MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL2Muons" )
)
process.hltL2MuonIsolations = cms.EDProducer( "L2MuonIsolationProducer",
  StandAloneCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ExtractorPSet = cms.PSet(
    DR_Veto_H = cms.double( 0.1 ),
    Vertex_Constraint_Z = cms.bool( False ),
    Threshold_H = cms.double( 0.5 ),
    ComponentName = cms.string( "CaloExtractor" ),
    Threshold_E = cms.double( 0.2 ),
    DR_Max = cms.double( 0.24 ),
    DR_Veto_E = cms.double( 0.07 ),
    Weight_E = cms.double( 1.5 ),
    Vertex_Constraint_XY = cms.bool( False ),
    DepositLabel = cms.untracked.string( "EcalPlusHcal" ),
    CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForMuons" ),
    Weight_H = cms.double( 1.0 )
  ),
  IsolatorPSet = cms.PSet(
    ConeSizes = cms.vdouble( 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24 ),
    ComponentName = cms.string( "SimpleCutsIsolator" ),
    Thresholds = cms.vdouble( 4.0, 3.7, 4.0, 3.5, 3.4, 3.4, 3.2, 3.4, 3.1, 2.9, 2.9, 2.7, 3.1, 3.0, 2.4, 2.1, 2.0, 2.3, 2.2, 2.4, 2.5, 2.5, 2.6, 2.9, 3.1, 2.9 ),
    EtaBounds = cms.vdouble( 0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411 )
  )
)
process.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGenerator",
  InputObjects = cms.InputTag( "hltL1extraParticles" ),
  GMTReadoutCollection = cms.InputTag( "hltGtDigis" ),
  Propagator = cms.string( "SteppingHelixPropagatorAny" ),
  L1MinPt = cms.double( 0.0 ),
  L1MaxEta = cms.double( 2.5 ),
  L1MinQuality = cms.uint32( 1 ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  )
)
process.hltL2Muons = cms.EDProducer( "L2MuonProducer",
  InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
  L2TrajBuilderParameters = cms.PSet(
    DoRefit = cms.bool( False ),
    SeedPropagator = cms.string( "FastSteppingHelixPropagatorAny" ),
    FilterParameters = cms.PSet(
      NumberOfSigma = cms.double( 3.0 ),
      FitDirection = cms.string( "insideOut" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      MaxChi2 = cms.double( 1000.0 ),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double( 25.0 ),
        Granularity = cms.int32( 0 ),
        RescaleErrorFactor = cms.double( 100.0 ),
        UseInvalidHits = cms.bool( True ),
        RescaleError = cms.bool( False )
      ),
      EnableRPCMeasurement = cms.bool( True ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      EnableDTMeasurement = cms.bool( True ),
      RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
      Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
      EnableCSCMeasurement = cms.bool( True )
    ),
    NavigationType = cms.string( "Standard" ),
    SeedTransformerParameters = cms.PSet(
      Fitter = cms.string( "KFFitterSmootherForL2Muon" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
      UseSubRecHits = cms.bool( False ),
      NMinRecHits = cms.uint32( 2 ),
      RescaleError = cms.double( 100.0 )
    ),
    DoBackwardFilter = cms.bool( True ),
    SeedPosition = cms.string( "in" ),
    BWFilterParameters = cms.PSet(
      NumberOfSigma = cms.double( 3.0 ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      FitDirection = cms.string( "outsideIn" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      MaxChi2 = cms.double( 100.0 ),
      MuonTrajectoryUpdatorParameters = cms.PSet(
        MaxChi2 = cms.double( 25.0 ),
        Granularity = cms.int32( 2 ),
        RescaleErrorFactor = cms.double( 100.0 ),
        UseInvalidHits = cms.bool( True ),
        RescaleError = cms.bool( False )
      ),
      EnableRPCMeasurement = cms.bool( True ),
      BWSeedType = cms.string( "fromGenerator" ),
      EnableDTMeasurement = cms.bool( True ),
      RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
      Propagator = cms.string( "FastSteppingHelixPropagatorAny" ),
      EnableCSCMeasurement = cms.bool( True )
    ),
    DoSeedRefit = cms.bool( False )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "FastSteppingHelixPropagatorAny", "FastSteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
    DoSmoothing = cms.bool( False ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
      Propagator = cms.string( "FastSteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" )
  )
)
process.hltL2TauJets = cms.EDProducer( "L2TauJetsMerger",
  EtMin = cms.double( 15.0 ),
  JetSrc = cms.VInputTag( "hltIconeTau1Regional", "hltIconeTau2Regional", "hltIconeTau3Regional", "hltIconeTau4Regional", "hltIconeCentral1Regional", "hltIconeCentral2Regional", "hltIconeCentral3Regional", "hltIconeCentral4Regional" )
)
process.hltL2TauNarrowConeIsolationProducer = cms.EDProducer( "L2TauNarrowConeIsolationProducer",
  L2TauJetCollection = cms.InputTag( "hltL2TauJets" ),
  EBRecHits = cms.InputTag( "hltEcalRegionalJetsRecHit:EcalRecHitsEB" ),
  EERecHits = cms.InputTag( "hltEcalRegionalJetsRecHit:EcalRecHitsEE" ),
  CaloTowers = cms.InputTag( "hltTowerMakerForJets" ),
  associationRadius = cms.double( 0.5 ),
  crystalThresholdEE = cms.double( 0.45 ),
  crystalThresholdEB = cms.double( 0.15 ),
  towerThreshold = cms.double( 1.0 ),
  ECALIsolation = cms.PSet(
    innerCone = cms.double( 0.15 ),
    runAlgorithm = cms.bool( True ),
    outerCone = cms.double( 0.5 )
  ),
  ECALClustering = cms.PSet(
    runAlgorithm = cms.bool( True ),
    clusterRadius = cms.double( 0.08 )
  ),
  TowerIsolation = cms.PSet(
    innerCone = cms.double( 0.2 ),
    runAlgorithm = cms.bool( True ),
    outerCone = cms.double( 0.5 )
  )
)
process.hltL2TauRelaxingIsolationSelector = cms.EDProducer( "L2TauRelaxingIsolationSelector",
  L2InfoAssociation = cms.InputTag( "hltL2TauNarrowConeIsolationProducer" ),
  MinJetEt = cms.double( 15.0 ),
  SeedTowerEt = cms.double( -10.0 ),
  EcalIsolationEt = cms.vdouble( 5.0, 0.025, 0.00075 ),
  TowerIsolationEt = cms.vdouble( 1000.0, 0.0, 0.0 ),
  NumberOfClusters = cms.vdouble( 1000.0, 0.0, 0.0 ),
  ClusterPhiRMS = cms.vdouble( 1000.0, 0.0, 0.0 ),
  ClusterEtaRMS = cms.vdouble( 1000.0, 0.0, 0.0 ),
  ClusterDRRMS = cms.vdouble( 1000.0, 0.0, 0.0 )
)
process.hltL3Mu5Jet10UL3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu5Jet10UL2Filtered4" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL3Muons" )
)
process.hltL3MuonCandidatesNoVtx = cms.EDProducer( "L3MuonCandidateProducer",
  InputObjects = cms.InputTag( "hltL3MuonsNoVtx" )
)
process.hltL3MuonIsolations = cms.EDProducer( "L3MuonIsolationProducer",
  inputMuonCollection = cms.InputTag( "hltL3Muons" ),
  OutputMuIsoDeposits = cms.bool( True ),
  TrackPt_Min = cms.double( -1.0 ),
  DepositLabel = cms.untracked.string( "" ),
  CutsPSet = cms.PSet(
    ConeSizes = cms.vdouble( 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24, 0.24 ),
    ComponentName = cms.string( "SimpleCuts" ),
    Thresholds = cms.vdouble( 1.1, 1.1, 1.1, 1.1, 1.2, 1.1, 1.2, 1.1, 1.2, 1.0, 1.1, 1.0, 1.0, 1.1, 1.0, 1.0, 1.1, 0.9, 1.1, 0.9, 1.1, 1.0, 1.0, 0.9, 0.8, 0.1 ),
    maxNTracks = cms.int32( -1 ),
    EtaBounds = cms.vdouble( 0.0435, 0.1305, 0.2175, 0.3045, 0.3915, 0.4785, 0.5655, 0.6525, 0.7395, 0.8265, 0.9135, 1.0005, 1.0875, 1.1745, 1.2615, 1.3485, 1.4355, 1.5225, 1.6095, 1.6965, 1.785, 1.88, 1.9865, 2.1075, 2.247, 2.411 ),
    applyCutsORmaxNTracks = cms.bool( False )
  ),
  ExtractorPSet = cms.PSet(
    Chi2Prob_Min = cms.double( -1.0 ),
    Diff_z = cms.double( 0.2 ),
    inputTrackCollection = cms.InputTag( "hltPixelTracks" ),
    ReferenceRadius = cms.double( 6.0 ),
    BeamSpotLabel = cms.InputTag( "hltOfflineBeamSpot" ),
    ComponentName = cms.string( "PixelTrackExtractor" ),
    DR_Max = cms.double( 0.24 ),
    Diff_r = cms.double( 0.1 ),
    PropagateTracksToRadius = cms.bool( True ),
    DR_VetoPt = cms.double( 0.025 ),
    DR_Veto = cms.double( 0.01 ),
    NHits_Min = cms.uint32( 0 ),
    Chi2Ndof_Max = cms.double( 1.0e+64 ),
    Pt_Min = cms.double( -1.0 ),
    DepositLabel = cms.untracked.string( "PXLS" ),
    BeamlineOption = cms.string( "BeamSpotFromEvent" ),
    VetoLeadingTrack = cms.bool( True ),
    PtVeto_Min = cms.double( 2.0 )
  )
)
process.hltL3Muons = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit" )
)
process.hltL3MuonsIOHit = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      TrackerSkipSection = cms.int32( -1 ),
      Chi2CutCSC = cms.double( 150.0 ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "L3MuKFFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      PropDirForCosmics = cms.bool( False ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "SmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      Eta_fixed = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
      OnDemand = cms.double( -1.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      DeltaR = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      Rescale_eta = cms.double( 3.0 ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      Rescale_Dz = cms.double( 3.0 ),
      MeasurementTrackerName = cms.string( "hltMeasurementTracker" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "L3MuKFFitter" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "SmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "SmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2IOHit" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SmartPropagatorAny", "SteppingHelixPropagatorAny", "SmartPropagator", "SteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "SteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit", "hltL3MuonsIOHit" )
)
process.hltL3MuonsNoVtx = cms.EDProducer( "L3TkMuonProducer",
  InputObjects = cms.InputTag( "hltL3TkTracksFromL2NoVtx" )
)
process.hltL3MuonsOIHit = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      TrackerSkipSection = cms.int32( -1 ),
      Chi2CutCSC = cms.double( 150.0 ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "L3MuKFFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      PropDirForCosmics = cms.bool( False ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "SmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      Eta_fixed = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
      OnDemand = cms.double( -1.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      DeltaR = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      Rescale_eta = cms.double( 3.0 ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      Rescale_Dz = cms.double( 3.0 ),
      MeasurementTrackerName = cms.string( "hltMeasurementTracker" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "L3MuKFFitter" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "SmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "SmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIHit" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SmartPropagatorAny", "SteppingHelixPropagatorAny", "SmartPropagator", "SteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "SteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3MuonsOIState = cms.EDProducer( "L3MuonProducer",
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double( -1.0 ),
    GlbRefitterParameters = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      TrackerSkipSection = cms.int32( -1 ),
      Chi2CutCSC = cms.double( 150.0 ),
      HitThreshold = cms.int32( 1 ),
      MuonHitsOption = cms.int32( 1 ),
      Chi2CutRPC = cms.double( 1.0 ),
      Fitter = cms.string( "L3MuKFFitter" ),
      DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
      PropDirForCosmics = cms.bool( False ),
      Chi2CutDT = cms.double( 10.0 ),
      RefitRPCHits = cms.bool( True ),
      SkipStation = cms.int32( -1 ),
      Propagator = cms.string( "SmartPropagatorAny" ),
      TrackerSkipSystem = cms.int32( -1 )
    ),
    ScaleTECxFactor = cms.double( -1.0 ),
    TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
    MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
    MuonTrackingRegionBuilder = cms.PSet(
      EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
      Eta_fixed = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
      OnDemand = cms.double( -1.0 ),
      Eta_min = cms.double( 0.05 ),
      Rescale_phi = cms.double( 3.0 ),
      DeltaR = cms.double( 0.2 ),
      DeltaZ_Region = cms.double( 15.9 ),
      Rescale_eta = cms.double( 3.0 ),
      PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
      vertexCollection = cms.InputTag( "pixelVertices" ),
      Phi_fixed = cms.double( 0.2 ),
      EscapePt = cms.double( 1.5 ),
      UseFixedRegion = cms.bool( False ),
      PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
      EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
      Phi_min = cms.double( 0.05 ),
      UseVertex = cms.bool( False ),
      Rescale_Dz = cms.double( 3.0 ),
      MeasurementTrackerName = cms.string( "hltMeasurementTracker" )
    ),
    RefitRPCHits = cms.bool( True ),
    PCut = cms.double( 2.5 ),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool( False ),
      Fitter = cms.string( "L3MuKFFitter" ),
      TrackerRecHitBuilder = cms.string( "WithTrackAngle" ),
      Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
      MuonRecHitBuilder = cms.string( "MuonRecHitBuilder" ),
      RefitDirection = cms.string( "insideOut" ),
      RefitRPCHits = cms.bool( True ),
      Propagator = cms.string( "SmartPropagatorAny" )
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Pt_threshold1 = cms.double( 0.0 ),
      DeltaDCut_3 = cms.double( 15.0 ),
      MinP = cms.double( 2.5 ),
      MinPt = cms.double( 1.0 ),
      Chi2Cut_1 = cms.double( 50.0 ),
      Pt_threshold2 = cms.double( 999999999.0 ),
      LocChi2Cut = cms.double( 0.001 ),
      Eta_threshold = cms.double( 1.2 ),
      Quality_3 = cms.double( 7.0 ),
      Quality_2 = cms.double( 15.0 ),
      Chi2Cut_2 = cms.double( 50.0 ),
      Chi2Cut_3 = cms.double( 200.0 ),
      DeltaDCut_1 = cms.double( 40.0 ),
      DeltaRCut_2 = cms.double( 0.2 ),
      DeltaRCut_3 = cms.double( 1.0 ),
      DeltaDCut_2 = cms.double( 10.0 ),
      DeltaRCut_1 = cms.double( 0.1 ),
      Propagator = cms.string( "SmartPropagator" ),
      Quality_1 = cms.double( 20.0 )
    ),
    PtCut = cms.double( 1.0 ),
    TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
    tkTrajLabel = cms.InputTag( "hltL3TkTracksFromL2OIState" )
  ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SmartPropagatorAny", "SteppingHelixPropagatorAny", "SmartPropagator", "SteppingHelixPropagatorOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool( True ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    SmoothTkTrack = cms.untracked.bool( False ),
    MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
    Smoother = cms.string( "KFSmootherForMuonTrackLoader" ),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double( 1000000.0 ),
      Propagator = cms.string( "SteppingHelixPropagatorOpposite" ),
      BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 )
    ),
    VertexConstraint = cms.bool( False ),
    DoSmoothing = cms.bool( True )
  )
)
process.hltL3TauCkfHighPtTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL3TauHighPtPixelSeeds" ),
  TrajectoryBuilder = cms.string( "trajBuilderL3" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TauCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltL3TauPixelSeeds" ),
  TrajectoryBuilder = cms.string( "trajBuilderL3" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TauConeIsolation = cms.EDProducer( "ConeIsolation",
  JetTrackSrc = cms.InputTag( "hltL3TauJetTracksAssociator" ),
  vertexSrc = cms.InputTag( "hltPixelVertices" ),
  useVertex = cms.bool( True ),
  useBeamSpot = cms.bool( True ),
  BeamSpotProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  MinimumNumberOfPixelHits = cms.int32( 2 ),
  MinimumNumberOfHits = cms.int32( 5 ),
  MaximumTransverseImpactParameter = cms.double( 300.0 ),
  MinimumTransverseMomentum = cms.double( 1.0 ),
  MaximumChiSquared = cms.double( 100.0 ),
  DeltaZetTrackVertex = cms.double( 0.2 ),
  MatchingCone = cms.double( 0.2 ),
  SignalCone = cms.double( 0.15 ),
  IsolationCone = cms.double( 0.5 ),
  MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
  UseFixedSizeCone = cms.bool( True ),
  VariableConeParameter = cms.double( 3.5 ),
  VariableMaxCone = cms.double( 0.17 ),
  VariableMinCone = cms.double( 0.05 )
)
process.hltL3TauCtfWithMaterialHighPtTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracks" ),
  Fitter = cms.string( "FittingSmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltL3TauCkfHighPtTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TauCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "ctfWithMaterialTracks" ),
  Fitter = cms.string( "FittingSmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltL3TauCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TauHighPtConeIsolation = cms.EDProducer( "ConeIsolation",
  JetTrackSrc = cms.InputTag( "hltL3TauJetHighPtTracksAssociator" ),
  vertexSrc = cms.InputTag( "hltPixelVertices" ),
  useVertex = cms.bool( True ),
  useBeamSpot = cms.bool( True ),
  BeamSpotProducer = cms.InputTag( "hltOfflineBeamSpot" ),
  MinimumNumberOfPixelHits = cms.int32( 2 ),
  MinimumNumberOfHits = cms.int32( 5 ),
  MaximumTransverseImpactParameter = cms.double( 300.0 ),
  MinimumTransverseMomentum = cms.double( 1.0 ),
  MaximumChiSquared = cms.double( 100.0 ),
  DeltaZetTrackVertex = cms.double( 0.2 ),
  MatchingCone = cms.double( 0.2 ),
  SignalCone = cms.double( 0.15 ),
  IsolationCone = cms.double( 0.5 ),
  MinimumTransverseMomentumInIsolationRing = cms.double( 1.0 ),
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  MaximumNumberOfTracksIsolationRing = cms.int32( 0 ),
  UseFixedSizeCone = cms.bool( True ),
  VariableConeParameter = cms.double( 3.5 ),
  VariableMaxCone = cms.double( 0.17 ),
  VariableMinCone = cms.double( 0.05 )
)
process.hltL3TauHighPtIsolationSelector = cms.EDProducer( "IsolatedTauJetsSelector",
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  UseIsolationDiscriminator = cms.bool( True ),
  UseInHLTOpen = cms.bool( False ),
  JetSrc = cms.VInputTag( "hltL3TauHighPtConeIsolation" )
)
process.hltL3TauHighPtPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      deltaPhiRegion = cms.double( 0.5 ),
      originHalfLength = cms.double( 0.2 ),
      originRadius = cms.double( 0.2 ),
      deltaEtaRegion = cms.double( 0.5 ),
      vertexSrc = cms.InputTag( "hltPixelVertices" ),
      JetSrc = cms.InputTag( "hltL25TauLeadingTrackHighPtCutSelector" ),
      originZPos = cms.double( 0.0 ),
      ptMin = cms.double( 0.9 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerPairs" ),
    maxElement = cms.uint32( 0 )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltL3TauIsolationSelector = cms.EDProducer( "IsolatedTauJetsSelector",
  MinimumTransverseMomentumLeadingTrack = cms.double( 5.0 ),
  UseIsolationDiscriminator = cms.bool( True ),
  UseInHLTOpen = cms.bool( False ),
  JetSrc = cms.VInputTag( "hltL3TauConeIsolation" )
)
process.hltL3TauJetHighPtTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
  jets = cms.InputTag( "hltL25TauLeadingTrackHighPtCutSelector" ),
  tracks = cms.InputTag( "hltL3TauCtfWithMaterialHighPtTracks" ),
  coneSize = cms.double( 0.5 )
)
process.hltL3TauJetTracksAssociator = cms.EDProducer( "JetTracksAssociatorAtVertex",
  jets = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
  tracks = cms.InputTag( "hltL3TauCtfWithMaterialTracks" ),
  coneSize = cms.double( 0.5 )
)
process.hltL3TauPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
  ClusterCheckPSet = cms.PSet(
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
    doClusterCheck = cms.bool( False ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 )
  ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "TauRegionalPixelSeedGenerator" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      deltaPhiRegion = cms.double( 0.5 ),
      originHalfLength = cms.double( 0.2 ),
      originRadius = cms.double( 0.2 ),
      deltaEtaRegion = cms.double( 0.5 ),
      vertexSrc = cms.InputTag( "hltPixelVertices" ),
      JetSrc = cms.InputTag( "hltL25TauLeadingTrackPtCutSelector" ),
      originZPos = cms.double( 0.0 ),
      ptMin = cms.double( 0.9 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitPairGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerPairs" ),
    maxElement = cms.uint32( 0 )
  ),
  SeedComparitorPSet = cms.PSet(
    ComponentName = cms.string( "none" )
  ),
  SeedCreatorPSet = cms.PSet(
    ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    propagator = cms.string( "PropagatorWithMaterial" )
  ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltL3TkFromL2OICombination = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3MuonsOIState", "hltL3MuonsOIHit" )
)
process.hltL3TkTracksFromL2 = cms.EDProducer( "L3TrackCombiner",
  labels = cms.VInputTag( "hltL3TkTracksFromL2IOHit", "hltL3TkTracksFromL2OIHit", "hltL3TkTracksFromL2OIState" )
)
process.hltL3TkTracksFromL2IOHit = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2IOHit" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2NoVtx = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2NoVtx" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIHit = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2OIHit" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TkTracksFromL2OIState = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "" ),
  Fitter = cms.string( "hltKFFittingSmoother" ),
  Propagator = cms.string( "PropagatorWithMaterial" ),
  src = cms.InputTag( "hltL3TrackCandidateFromL2OIState" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltL3TrackCandidateFromL2 = cms.EDProducer( "L3TrackCandCombiner",
  labels = cms.VInputTag( "hltL3TrackCandidateFromL2IOHit", "hltL3TrackCandidateFromL2OIHit", "hltL3TrackCandidateFromL2OIState" )
)
process.hltL3TrackCandidateFromL2IOHit = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedIOHit" ),
  TrajectoryBuilder = cms.string( "muonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2NoVtx = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajectorySeedNoVtx" ),
  TrajectoryBuilder = cms.string( "muonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIHit = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedOIHit" ),
  TrajectoryBuilder = cms.string( "muonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrackCandidateFromL2OIState = cms.EDProducer( "CkfTrajectoryMaker",
  trackCandidateAlso = cms.bool( True ),
  src = cms.InputTag( "hltL3TrajSeedOIState" ),
  TrajectoryBuilder = cms.string( "muonCkfTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    numberMeasurementsForFit = cms.int32( 4 ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
  ),
  doSeedingRegionRebuilding = cms.bool( False ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltL3TrajSeedIOHit = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True ),
    Propagators = cms.untracked.vstring( "PropagatorWithMaterial" )
  ),
  MuonTrackingRegionBuilder = cms.PSet(
    EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
    Eta_fixed = cms.double( 0.2 ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    OnDemand = cms.double( -1.0 ),
    Eta_min = cms.double( 0.1 ),
    Rescale_phi = cms.double( 3.0 ),
    DeltaR = cms.double( 0.2 ),
    DeltaZ_Region = cms.double( 15.9 ),
    Rescale_eta = cms.double( 3.0 ),
    PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
    vertexCollection = cms.InputTag( "pixelVertices" ),
    Phi_fixed = cms.double( 0.2 ),
    EscapePt = cms.double( 1.5 ),
    UseFixedRegion = cms.bool( False ),
    PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
    EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
    Phi_min = cms.double( 0.1 ),
    UseVertex = cms.bool( False ),
    Rescale_Dz = cms.double( 3.0 ),
    MeasurementTrackerName = cms.string( "hltMeasurementTracker" )
  ),
  TkSeedGenerator = cms.PSet(
    ComponentName = cms.string( "DualByL2TSG" ),
    L3TkCollectionA = cms.InputTag( "hltL3TkFromL2OICombination" ),
    iterativeTSG = cms.PSet(
      firstTSG = cms.PSet(
        ComponentName = cms.string( "TSGFromOrderedHits" ),
        OrderedHitsFactoryPSet = cms.PSet(
          ComponentName = cms.string( "StandardHitTripletGenerator" ),
          SeedingLayers = cms.string( "hltPixelLayerTriplets" ),
          GeneratorPSet = cms.PSet(
            useBending = cms.bool( True ),
            useFixedPreFiltering = cms.bool( False ),
            maxElement = cms.uint32( 10000 ),
            phiPreFiltering = cms.double( 0.3 ),
            extraHitRPhitolerance = cms.double( 0.06 ),
            useMultScattering = cms.bool( True ),
            ComponentName = cms.string( "PixelTripletHLTGenerator" ),
            extraHitRZtolerance = cms.double( 0.06 )
          )
        ),
        TTRHBuilder = cms.string( "WithTrackAngle" )
      ),
      PSetNames = cms.vstring( "firstTSG", "secondTSG" ),
      thirdTSG = cms.PSet(
        PSetNames = cms.vstring( "endcapTSG", "barrelTSG" ),
        ComponentName = cms.string( "DualByEtaTSG" ),
        endcapTSG = cms.PSet(
          ComponentName = cms.string( "TSGFromOrderedHits" ),
          OrderedHitsFactoryPSet = cms.PSet(
            maxElement = cms.uint32( 0 ),
            ComponentName = cms.string( "StandardHitPairGenerator" ),
            SeedingLayers = cms.string( "hltMixedLayerPairs" ),
            useOnDemandTracker = cms.untracked.int32( 0 )
          ),
          TTRHBuilder = cms.string( "WithTrackAngle" )
        ),
        etaSeparation = cms.double( 2.0 ),
        barrelTSG = cms.PSet(

        )
      ),
      ComponentName = cms.string( "CombinedTSG" ),
      secondTSG = cms.PSet(
        ComponentName = cms.string( "TSGFromOrderedHits" ),
        OrderedHitsFactoryPSet = cms.PSet(
          maxElement = cms.uint32( 0 ),
          ComponentName = cms.string( "StandardHitPairGenerator" ),
          SeedingLayers = cms.string( "hltPixelLayerPairs" ),
          useOnDemandTracker = cms.untracked.int32( 0 )
        ),
        TTRHBuilder = cms.string( "WithTrackAngle" )
      )
    ),
    skipTSG = cms.PSet(

    ),
    PSetNames = cms.vstring( "skipTSG", "iterativeTSG" )
  ),
  TrackerSeedCleaner = cms.PSet(
    cleanerFromSharedHits = cms.bool( True ),
    ptCleaner = cms.bool( True ),
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    directionCleaner = cms.bool( True )
  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajSeedOIHit = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "PropagatorWithMaterial", "SmartPropagatorAnyOpposite" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    ComponentName = cms.string( "DualByL2TSG" ),
    L3TkCollectionA = cms.InputTag( "hltL3MuonsOIState" ),
    iterativeTSG = cms.PSet(
      ErrorRescaling = cms.double( 3.0 ),
      beamSpot = cms.InputTag( "offlineBeamSpot" ),
      ComponentName = cms.string( "TSGFromPropagation" ),
      errorMatrixPset = cms.PSet(
        action = cms.string( "use" ),
        atIP = cms.bool( True ),
        errorMatrixValuesPSet = cms.PSet(
          pf3_V12 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V13 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V11 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V14 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V15 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
          zAxis = cms.vdouble( -3.14159, 3.14159 ),
          pf3_V33 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V45 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V44 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
          pf3_V23 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V22 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V55 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
          ),
          pf3_V34 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V35 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V25 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          ),
          pf3_V24 = cms.PSet(
            action = cms.string( "scale" ),
            values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
          )
        )
      ),
      UpdateState = cms.bool( True ),
      SelectState = cms.bool( False ),
      SigmaZ = cms.double( 25.0 ),
      ResetMethod = cms.string( "matrix" ),
      MaxChi2 = cms.double( 40.0 ),
      UseVertexState = cms.bool( True ),
      Propagator = cms.string( "SmartPropagatorAnyOpposite" ),
      MeasurementTrackerName = cms.string( "hltMeasurementTracker" )
    ),
    skipTSG = cms.PSet(

    ),
    PSetNames = cms.vstring( "skipTSG", "iterativeTSG" )
  ),
  TrackerSeedCleaner = cms.PSet(
    cleanerFromSharedHits = cms.bool( True ),
    ptCleaner = cms.bool( True ),
    TTRHBuilder = cms.string( "WithTrackAngle" ),
    beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
    directionCleaner = cms.bool( True )
  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajSeedOIState = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons:UpdatedAtVtx" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SteppingHelixPropagatorOpposite", "SteppingHelixPropagatorAlong" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    propagatorCompatibleName = cms.string( "SteppingHelixPropagatorOpposite" ),
    option = cms.uint32( 3 ),
    ComponentName = cms.string( "TSGForRoadSearch" ),
    errorMatrixPset = cms.PSet(
      action = cms.string( "use" ),
      atIP = cms.bool( True ),
      errorMatrixValuesPSet = cms.PSet(
        pf3_V12 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V13 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V11 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V14 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V15 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
        zAxis = cms.vdouble( -3.14159, 3.14159 ),
        pf3_V33 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V45 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V44 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
        pf3_V23 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V22 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V55 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V34 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V35 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V25 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V24 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        )
      )
    ),
    propagatorName = cms.string( "SteppingHelixPropagatorAlong" ),
    manySeeds = cms.bool( False ),
    copyMuonRecHit = cms.bool( False ),
    maxChi2 = cms.double( 40.0 )
  ),
  TrackerSeedCleaner = cms.PSet(

  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltL3TrajectorySeed = cms.EDProducer( "L3MuonTrajectorySeedCombiner",
  labels = cms.VInputTag( "hltL3TrajSeedIOHit", "hltL3TrajSeedOIState", "hltL3TrajSeedOIHit" )
)
process.hltL3TrajectorySeedNoVtx = cms.EDProducer( "TSGFromL2Muon",
  PtCut = cms.double( 1.0 ),
  PCut = cms.double( 2.5 ),
  MuonCollectionLabel = cms.InputTag( "hltL2Muons" ),
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring( "SteppingHelixPropagatorOpposite", "SteppingHelixPropagatorAlong" ),
    RPCLayers = cms.bool( True ),
    UseMuonNavigation = cms.untracked.bool( True )
  ),
  MuonTrackingRegionBuilder = cms.PSet(

  ),
  TkSeedGenerator = cms.PSet(
    propagatorCompatibleName = cms.string( "SteppingHelixPropagatorOpposite" ),
    option = cms.uint32( 3 ),
    ComponentName = cms.string( "TSGForRoadSearch" ),
    errorMatrixPset = cms.PSet(
      action = cms.string( "use" ),
      atIP = cms.bool( True ),
      errorMatrixValuesPSet = cms.PSet(
        pf3_V12 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V13 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V11 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V14 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        yAxis = cms.vdouble( 0.0, 1.0, 1.4, 10.0 ),
        pf3_V15 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        zAxis = cms.vdouble( -3.14159, 3.14159 ),
        pf3_V33 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V45 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V44 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        xAxis = cms.vdouble( 0.0, 13.0, 30.0, 70.0, 1000.0 ),
        pf3_V23 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V22 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V55 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 3.0, 3.0, 3.0, 5.0, 4.0, 5.0, 10.0, 7.0, 10.0, 10.0, 10.0, 10.0 )
        ),
        pf3_V34 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V35 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V25 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        ),
        pf3_V24 = cms.PSet(
          action = cms.string( "scale" ),
          values = cms.vdouble( 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 )
        )
      )
    ),
    propagatorName = cms.string( "SteppingHelixPropagatorAlong" ),
    manySeeds = cms.bool( False ),
    copyMuonRecHit = cms.bool( False ),
    maxChi2 = cms.double( 40.0 )
  ),
  TrackerSeedCleaner = cms.PSet(

  ),
  TSGFromMixedPairs = cms.PSet(

  ),
  TSGFromPixelTriplets = cms.PSet(

  ),
  TSGFromPixelPairs = cms.PSet(

  ),
  TSGForRoadSearchOI = cms.PSet(

  ),
  TSGForRoadSearchIOpxl = cms.PSet(

  ),
  TSGFromPropagation = cms.PSet(

  ),
  TSGFromCombinedHits = cms.PSet(

  )
)
process.hltLevel1Activity = cms.HLTFilter( "HLTLevel1Activity",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( False ),
  invert = cms.bool( False ),
  bunchCrossings = cms.vint32( 0, 1, -1 ),
  physicsLoBits = cms.uint64( 0x7fdfdf03c03fbffc ),
  physicsHiBits = cms.uint64( 0x3f1bfddb01800bf6 ),
  technicalBits = cms.uint64( 0x70000fffff001f00 )
)
process.hltLogMonitorFilter = cms.HLTFilter( "HLTLogMonitorFilter",
  default_threshold = cms.uint32( 10 ),
  categories = cms.VPSet(

  )
)
process.hltMCJetCorJetIcone5HF07 = cms.EDProducer( "CaloJetCorrectionProducer",
  src = cms.InputTag( "hltIterativeCone5CaloJets" ),
  verbose = cms.untracked.bool( False ),
  alias = cms.untracked.string( "MCJetCorJetIcone5" ),
  correctors = cms.vstring( "MCJetCorrectorIcone5HF07" )
)
process.hltMCJetCorJetIcone5Regional = cms.EDProducer( "CaloJetCorrectionProducer",
  src = cms.InputTag( "hltIterativeCone5CaloJetsRegional" ),
  verbose = cms.untracked.bool( False ),
  alias = cms.untracked.string( "corJetIcone5" ),
  correctors = cms.vstring( "MCJetCorrectorIcone5" )
)
process.hltMet = cms.EDProducer( "METProducer",
  src = cms.InputTag( "hltTowerMakerForAll" ),
  InputType = cms.string( "CandidateCollection" ),
  METType = cms.string( "CaloMET" ),
  alias = cms.string( "RawCaloMET" ),
  globalThreshold = cms.double( 0.3 ),
  noHF = cms.bool( False ),
  calculateSignificance = cms.bool( False ),
  onlyFiducialParticles = cms.bool( False ),
  usePt = cms.untracked.bool( False ),
  rf_type = cms.int32( 0 ),
  correctShowerTracks = cms.bool( False ),
  HO_EtResPar = cms.vdouble( 0.0, 1.3, 0.005 ),
  HF_EtResPar = cms.vdouble( 0.0, 1.82, 0.09 ),
  HB_PhiResPar = cms.vdouble( 0.02511 ),
  HE_PhiResPar = cms.vdouble( 0.02511 ),
  EE_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  EB_PhiResPar = cms.vdouble( 0.00502 ),
  EE_PhiResPar = cms.vdouble( 0.02511 ),
  HB_EtResPar = cms.vdouble( 0.0, 1.22, 0.05 ),
  EB_EtResPar = cms.vdouble( 0.2, 0.03, 0.005 ),
  HF_PhiResPar = cms.vdouble( 0.05022 ),
  HE_EtResPar = cms.vdouble( 0.0, 1.3, 0.05 ),
  HO_PhiResPar = cms.vdouble( 0.02511 )
)
process.hltMinBiasPixelFilter1 = cms.HLTFilter( "HLTPixlMBFilt",
  pixlTag = cms.InputTag( "hltPixelCandsForMinBias" ),
  MinPt = cms.double( 0.0 ),
  MinTrks = cms.uint32( 1 ),
  MinSep = cms.double( 1.0 )
)
process.hltMu0TkMuJpsiTkMuMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTkMuJpsiTrackerMuonCands" ),
  PreviousCandTag = cms.InputTag( "hltMu0TkMuJpsiTrackMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu0TkMuJpsiTkMuMassFilteredTight = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTkMuJpsiTrackerMuonCands" ),
  PreviousCandTag = cms.InputTag( "hltMu0TkMuJpsiTrackMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( True ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu0TkMuJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu0TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu0TrackJpsiL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltMu0TrackJpsiL2Filtered0 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu0TrackJpsiL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltMu0TrackJpsiL3Filtered0 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu0TrackJpsiL2Filtered0" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu0TrackJpsiPixelMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiPixelTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu0TrackJpsiL3Filtered0" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 3 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 999.0 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMu20NoVertexL2PreFiltered = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu7L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 15.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu20NoVertexL3PreFiltered20 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltMu20NoVertexL2PreFiltered" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 20.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu3TkMuJpsiTkMuMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTkMuJpsiTrackerMuonCands" ),
  PreviousCandTag = cms.InputTag( "hltMu3TkMuJpsiTrackMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu3TkMuJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu3Track3JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 3.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 3.6 )
)
process.hltMu3Track5JpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 5.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 3.6 )
)
process.hltMu3TrackJpsiL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltMu3TrackJpsiL2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltMu3TrackJpsiL3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiL2Filtered3" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu3TrackJpsiPixelMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiPixelTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu3TrackJpsiL3Filtered3" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 3 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 999.0 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMu5L2Mu0L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltDiMuonL2PreFiltered0" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu5TkMuJpsiTkMuMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTkMuJpsiTrackerMuonCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TkMuJpsiTrackMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu5TkMuJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 4.1 )
)
process.hltMu5TrackJpsiL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu3" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltMu5TrackJpsiL2Filtered4 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 4.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltMu5TrackJpsiL3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL2Filtered4" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltMu5TrackJpsiPixelMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiPixelTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiL3Filtered5" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 3 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 999.0 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMu5TrackJpsiTrackMassFiltered = cms.HLTFilter( "HLTMuonTrackMassFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  TrackTag = cms.InputTag( "hltMuTrackJpsiCtfTrackCands" ),
  PreviousCandTag = cms.InputTag( "hltMu5TrackJpsiPixelMassFiltered" ),
  SaveTag = cms.untracked.bool( True ),
  checkCharge = cms.bool( True ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.7 ),
  MaxTrackEta = cms.double( 999.0 ),
  MaxTrackDxy = cms.double( 999.0 ),
  MaxTrackDz = cms.double( 999.0 ),
  MinTrackHits = cms.int32( 5 ),
  MaxTrackNormChi2 = cms.double( 10000000000.0 ),
  MaxDzMuonTrack = cms.double( 0.5 ),
  CutCowboys = cms.bool( False ),
  MinMasses = cms.vdouble( 2.5 ),
  MaxMasses = cms.vdouble( 3.6 )
)
process.hltMuTkMuJpsiTrackerMuonCands = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
  InputObjects = cms.InputTag( "hltMuTkMuJpsiTrackerMuons" )
)
process.hltMuTkMuJpsiTrackerMuons = cms.EDProducer( "MuonIdProducer",
  minPt = cms.double( 0.0 ),
  minP = cms.double( 2.7 ),
  minPCaloMuon = cms.double( 1.0 ),
  minNumberOfMatches = cms.int32( 1 ),
  addExtraSoftMuons = cms.bool( False ),
  maxAbsEta = cms.double( 999.0 ),
  maxAbsDx = cms.double( 3.0 ),
  maxAbsPullX = cms.double( 3.0 ),
  maxAbsDy = cms.double( 3.0 ),
  maxAbsPullY = cms.double( 3.0 ),
  fillCaloCompatibility = cms.bool( False ),
  fillEnergy = cms.bool( False ),
  fillMatching = cms.bool( True ),
  fillIsolation = cms.bool( False ),
  writeIsoDeposits = cms.bool( False ),
  fillGlobalTrackQuality = cms.bool( False ),
  ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
  sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
  minCaloCompatibility = cms.double( 0.6 ),
  runArbitrationCleaner = cms.bool( False ),
  trackDepositName = cms.string( "tracker" ),
  ecalDepositName = cms.string( "ecal" ),
  hcalDepositName = cms.string( "hcal" ),
  hoDepositName = cms.string( "ho" ),
  jetDepositName = cms.string( "jets" ),
  debugWithTruthMatching = cms.bool( False ),
  globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
  inputCollectionLabels = cms.VInputTag( "hltMuTrackJpsiCtfTracks" ),
  inputCollectionTypes = cms.vstring( "inner tracks" ),
  arbitrationCleanerOptions = cms.PSet(
    ME1a = cms.bool( True ),
    Overlap = cms.bool( True ),
    Clustering = cms.bool( True ),
    OverlapDPhi = cms.double( 0.0786 ),
    OverlapDTheta = cms.double( 0.02 ),
    ClusterDPhi = cms.double( 0.6 ),
    ClusterDTheta = cms.double( 0.02 )
  ),
  TrackAssociatorParameters = cms.PSet(
    muonMaxDistanceSigmaX = cms.double( 0.0 ),
    muonMaxDistanceSigmaY = cms.double( 0.0 ),
    CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
    dRHcal = cms.double( 9999.0 ),
    dREcal = cms.double( 9999.0 ),
    CaloTowerCollectionLabel = cms.InputTag( "towerMaker" ),
    useEcal = cms.bool( False ),
    dREcalPreselection = cms.double( 0.05 ),
    HORecHitCollectionLabel = cms.InputTag( "hltHoreco" ),
    dRMuon = cms.double( 9999.0 ),
    trajectoryUncertaintyTolerance = cms.double( -1.0 ),
    propagateAllDirections = cms.bool( True ),
    muonMaxDistanceX = cms.double( 5.0 ),
    muonMaxDistanceY = cms.double( 5.0 ),
    useHO = cms.bool( False ),
    accountForTrajectoryChangeCalo = cms.bool( False ),
    DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
    EERecHitCollectionLabel = cms.InputTag( "ecalRecHit:EcalRecHitsEE" ),
    dRMuonPreselection = cms.double( 0.2 ),
    usePreshower = cms.bool( False ),
    dRPreshowerPreselection = cms.double( 0.2 ),
    dRHcalPreselection = cms.double( 0.2 ),
    useMuon = cms.bool( True ),
    useCalo = cms.bool( False ),
    EBRecHitCollectionLabel = cms.InputTag( "ecalRecHit:EcalRecHitsEB" ),
    truthMatch = cms.bool( False ),
    HBHERecHitCollectionLabel = cms.InputTag( "hbhereco" ),
    useHcal = cms.bool( False )
  ),
  TimingFillerParameters = cms.PSet(
    DTTimingParameters = cms.PSet(
      MatchParameters = cms.PSet(
        DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        TightMatchDT = cms.bool( False ),
        TightMatchCSC = cms.bool( True )
      ),
      ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny", "PropagatorWithMaterial", "PropagatorWithMaterialOpposite" ),
        RPCLayers = cms.bool( True )
      ),
      DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
      PruneCut = cms.double( 1000.0 ),
      HitsMin = cms.int32( 3 ),
      DoWireCorr = cms.bool( False ),
      RequireBothProjections = cms.bool( False ),
      debug = cms.bool( False ),
      UseSegmentT0 = cms.bool( False )
    ),
    CSCTimingParameters = cms.PSet(
      MatchParameters = cms.PSet(
        DTsegments = cms.InputTag( "hltDthlt4DSegments" ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        TightMatchDT = cms.bool( False ),
        TightMatchCSC = cms.bool( True )
      ),
      ServiceParameters = cms.PSet(
        Propagators = cms.untracked.vstring( "SteppingHelixPropagatorAny", "PropagatorWithMaterial", "PropagatorWithMaterialOpposite" ),
        RPCLayers = cms.bool( True )
      ),
      CSCsegments = cms.InputTag( "hltCscSegments" ),
      PruneCut = cms.double( 100.0 ),
      CSCTimeOffset = cms.double( 213.0 ),
      debug = cms.bool( False )
    ),
    ErrorDT = cms.double( 3.1 ),
    ErrorCSC = cms.double( 7.0 ),
    ErrorEB = cms.double( 2.085 ),
    ErrorEE = cms.double( 6.95 ),
    EcalEnergyCut = cms.double( 0.4 ),
    UseDT = cms.bool( True ),
    UseCSC = cms.bool( True ),
    UseECAL = cms.bool( False )
  ),
  JetExtractorPSet = cms.PSet(

  ),
  TrackExtractorPSet = cms.PSet(

  ),
  MuonCaloCompatibility = cms.PSet(

  ),
  CaloExtractorPSet = cms.PSet(

  )
)
process.hltMuTrackJpsiCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
  src = cms.InputTag( "hltMuTrackJpsiTrackSeeds" ),
  TrajectoryBuilder = cms.string( "hltMuTrackJpsiTrajectoryBuilder" ),
  TrajectoryCleaner = cms.string( "TrajectoryCleanerBySharedHits" ),
  NavigationSchool = cms.string( "SimpleNavigationSchool" ),
  RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
  useHitsSplitting = cms.bool( False ),
  doSeedingRegionRebuilding = cms.bool( False ),
  TransientInitialStateEstimatorParameters = cms.PSet(
    propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
    propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" ),
    numberMeasurementsForFit = cms.int32( 4 )
  ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  maxNSeeds = cms.uint32( 100000 )
)
process.hltMuTrackJpsiCtfTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltMuTrackJpsiCtfTracks" ),
  particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiCtfTracks = cms.EDProducer( "TrackProducer",
  TrajectoryInEvent = cms.bool( True ),
  useHitsSplitting = cms.bool( False ),
  clusterRemovalInfo = cms.InputTag( "" ),
  alias = cms.untracked.string( "hltMuTrackJpsiCtfTracks" ),
  Fitter = cms.string( "FittingSmootherRK" ),
  Propagator = cms.string( "RungeKuttaTrackerPropagator" ),
  src = cms.InputTag( "hltMuTrackJpsiCkfTrackCandidates" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  TTRHBuilder = cms.string( "WithTrackAngle" ),
  AlgorithmName = cms.string( "undefAlgorithm" ),
  NavigationSchool = cms.string( "" )
)
process.hltMuTrackJpsiPixelTrackCands = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltMuTrackJpsiPixelTrackSelector" ),
  particleType = cms.string( "mu-" )
)
process.hltMuTrackJpsiPixelTrackSelector = cms.EDProducer( "QuarkoniaTrackSelector",
  muonCandidates = cms.InputTag( "hltL3MuonCandidates" ),
  tracks = cms.InputTag( "hltPixelTracks" ),
  checkCharge = cms.bool( False ),
  MinTrackPt = cms.double( 0.0 ),
  MinTrackP = cms.double( 2.5 ),
  MaxTrackEta = cms.double( 999.0 ),
  MinMasses = cms.vdouble( 2.0 ),
  MaxMasses = cms.vdouble( 4.6 )
)
process.hltMuTrackJpsiTrackSeeds = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
  InputCollection = cms.InputTag( "hltMuTrackJpsiPixelTrackSelector" ),
  useProtoTrackKinematics = cms.bool( False ),
  TTRHBuilder = cms.string( "WithTrackAngle" )
)
process.hltMulti5x5BasicClustersActivity = cms.EDProducer( "Multi5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  barrelHitProducer = cms.string( "hltEcalRecHitAll" ),
  endcapHitProducer = cms.string( "hltEcalRecHitAll" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  doEndcap = cms.bool( True ),
  doBarrel = cms.bool( False ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  IslandBarrelSeedThr = cms.double( 0.5 ),
  IslandEndcapSeedThr = cms.double( 0.18 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  clustershapecollectionEB = cms.string( "multi5x5BarrelShape" ),
  clustershapecollectionEE = cms.string( "multi5x5EndcapShape" ),
  barrelShapeAssociation = cms.string( "multi5x5BarrelShapeAssoc" ),
  endcapShapeAssociation = cms.string( "multi5x5EndcapShapeAssoc" ),
  RecHitFlagToBeExcluded = cms.vint32(  )
)
process.hltMulti5x5BasicClustersL1Isolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( True ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  RecHitFlagToBeExcluded = cms.vint32(  )
)
process.hltMulti5x5BasicClustersL1IsolatedLowPt = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( True ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 3.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  RecHitFlagToBeExcluded = cms.vint32(  )
)
process.hltMulti5x5BasicClustersL1NonIsolated = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( False ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHit" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 5.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  RecHitFlagToBeExcluded = cms.vint32(  )
)
process.hltMulti5x5BasicClustersL1NonIsolatedLowPt = cms.EDProducer( "EgammaHLTMulti5x5ClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  doIsolated = cms.bool( False ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalEgammaRecHitLowPt" ),
  barrelHitCollection = cms.string( "EcalRecHitsEB" ),
  endcapHitCollection = cms.string( "EcalRecHitsEE" ),
  barrelClusterCollection = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  Multi5x5BarrelSeedThr = cms.double( 0.5 ),
  Multi5x5EndcapSeedThr = cms.double( 0.18 ),
  l1TagIsolated = cms.InputTag( "hltL1extraParticles:Isolated" ),
  l1TagNonIsolated = cms.InputTag( "hltL1extraParticles:NonIsolated" ),
  l1LowerThr = cms.double( 3.0 ),
  l1UpperThr = cms.double( 999.0 ),
  l1LowerThrIgnoreIsolation = cms.double( 999.0 ),
  regionEtaMargin = cms.double( 0.3 ),
  regionPhiMargin = cms.double( 0.4 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  RecHitFlagToBeExcluded = cms.vint32(  )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHit:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1Isolated:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 5.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHitLowPt:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1IsolatedLowPt:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 3.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHit:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1NonIsolated:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 5.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRegionalEgammaRecHitLowPt:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersL1NonIsolatedLowPt:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 3.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "" )
)
process.hltMulti5x5SuperClustersActivity = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
  barrelClusterProducer = cms.string( "hltMulti5x5BasicClustersActivity" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 1.0 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(
      cryVec = cms.vint32( 16, 13, 11, 10, 9, 8, 7, 6, 5, 4, 3 ),
      cryMin = cms.int32( 2 ),
      etVec = cms.vdouble( 5.0, 10.0, 15.0, 20.0, 30.0, 40.0, 45.0, 55.0, 135.0, 195.0, 225.0 )
    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    )
  )
)
process.hltMulti5x5SuperClustersL1Isolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1Isolated" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 1.0 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMulti5x5SuperClustersL1IsolatedLowPt = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1IsolatedLowPt" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 0.5 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMulti5x5SuperClustersL1NonIsolated = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1NonIsolated" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 1.0 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMulti5x5SuperClustersL1NonIsolatedLowPt = cms.EDProducer( "Multi5x5SuperClusterProducer",
  VerbosityLevel = cms.string( "ERROR" ),
  endcapClusterProducer = cms.string( "hltMulti5x5BasicClustersL1NonIsolatedLowPt" ),
  barrelClusterProducer = cms.string( "notused" ),
  endcapClusterCollection = cms.string( "multi5x5EndcapBasicClusters" ),
  barrelClusterCollection = cms.string( "multi5x5BarrelBasicClusters" ),
  endcapSuperclusterCollection = cms.string( "multi5x5EndcapSuperClusters" ),
  barrelSuperclusterCollection = cms.string( "multi5x5BarrelSuperClusters" ),
  doBarrel = cms.bool( False ),
  doEndcaps = cms.bool( True ),
  barrelEtaSearchRoad = cms.double( 0.06 ),
  barrelPhiSearchRoad = cms.double( 0.8 ),
  endcapEtaSearchRoad = cms.double( 0.14 ),
  endcapPhiSearchRoad = cms.double( 0.6 ),
  seedTransverseEnergyThreshold = cms.double( 0.5 ),
  dynamicPhiRoad = cms.bool( False ),
  bremRecoveryPset = cms.PSet(
    barrel = cms.PSet(

    ),
    endcap = cms.PSet(
      a = cms.double( 47.85 ),
      c = cms.double( 0.1201 ),
      b = cms.double( 108.8 )
    ),
    doEndcaps = cms.bool( True ),
    doBarrel = cms.bool( False )
  )
)
process.hltMulti5x5SuperClustersWithPreshowerActivity = cms.EDProducer( "PreshowerClusterProducer",
  preshRecHitProducer = cms.InputTag( "hltESRecHitAll:EcalRecHitsES" ),
  endcapSClusterProducer = cms.InputTag( "hltMulti5x5SuperClustersActivity:multi5x5EndcapSuperClusters" ),
  preshClusterCollectionX = cms.string( "preshowerXClusters" ),
  preshClusterCollectionY = cms.string( "preshowerYClusters" ),
  preshNclust = cms.int32( 4 ),
  etThresh = cms.double( 0.0 ),
  assocSClusterCollection = cms.string( "" ),
  preshStripEnergyCut = cms.double( 0.0 ),
  preshSeededNstrip = cms.int32( 15 ),
  preshClusterEnergyCut = cms.double( 0.0 ),
  debugLevel = cms.string( "ERROR" )
)
process.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
  InputObjects = cms.InputTag( "source" ),
  UseExaminer = cms.bool( True ),
  ExaminerMask = cms.uint32( 0x1febf3f6 ),
  UseSelectiveUnpacking = cms.bool( True ),
  ErrorMask = cms.uint32( 0x00000000 ),
  UnpackStatusDigis = cms.bool( False ),
  UseFormatStatus = cms.bool( True ),
  PrintEventNumber = cms.untracked.bool( False ),
  Debug = cms.untracked.bool( False ),
  runDQM = cms.untracked.bool( False ),
  VisualFEDInspect = cms.untracked.bool( False ),
  VisualFEDShort = cms.untracked.bool( False ),
  FormatedEventDump = cms.untracked.bool( False ),
  SuppressZeroLCT = cms.untracked.bool( True )
)
process.hltMuonDTDigis = cms.EDProducer( "DTUnpackingModule",
  dataType = cms.string( "DDU" ),
  fedbyType = cms.bool( False ),
  inputLabel = cms.InputTag( "source" ),
  useStandardFEDid = cms.bool( True ),
  minFEDid = cms.untracked.int32( 770 ),
  maxFEDid = cms.untracked.int32( 779 ),
  dqmOnly = cms.bool( False ),
  rosParameters = cms.PSet(

  ),
  readOutParameters = cms.PSet(
    debug = cms.untracked.bool( False ),
    rosParameters = cms.PSet(
      writeSC = cms.untracked.bool( True ),
      readingDDU = cms.untracked.bool( True ),
      performDataIntegrityMonitor = cms.untracked.bool( False ),
      readDDUIDfromDDU = cms.untracked.bool( True ),
      debug = cms.untracked.bool( False ),
      localDAQ = cms.untracked.bool( False )
    ),
    performDataIntegrityMonitor = cms.untracked.bool( False ),
    localDAQ = cms.untracked.bool( False )
  )
)
process.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
  InputLabel = cms.InputTag( "source" ),
  doSynchro = cms.bool( False )
)
process.hltOfflineBeamSpot = cms.EDProducer( "BeamSpotProducer" )
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
  label = cms.InputTag( "hltScalersRawToDigi" ),
  changeToCMSCoordinates = cms.bool( False ),
  maxRadius = cms.double( 2.0 ),
  maxZ = cms.double( 40.0 ),
  setSigmaZ = cms.double( 10.0 ),
  gtEvmLabel = cms.InputTag( "" )
)
process.hltPixelCandsForHighMult = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltPixelTracksForHighMult" ),
  particleType = cms.string( "pi+" )
)
process.hltPixelCandsForMinBias = cms.EDProducer( "ConcreteChargedCandidateProducer",
  src = cms.InputTag( "hltPixelTracksForMinBias" ),
  particleType = cms.string( "pi+" )
)
process.hltPixelMatchElectronsL1Iso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
  TrackProducer = cms.InputTag( "hltCtfL1IsoWithMaterialTracks" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" )
)
process.hltPixelMatchElectronsL1NonIso = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
  TrackProducer = cms.InputTag( "hltCtfL1NonIsoWithMaterialTracks" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" )
)
process.hltPixelMatchStartUpWindowElectronsL1IsoLowPt = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
  TrackProducer = cms.InputTag( "hltCtfL1IsoStartUpWindowWithMaterialTracksLowPt" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" )
)
process.hltPixelMatchStartUpWindowElectronsL1NonIsoLowPt = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
  TrackProducer = cms.InputTag( "hltCtfL1NonIsoStartUpWindowWithMaterialTracksLowPt" ),
  BSProducer = cms.InputTag( "hltOfflineBeamSpot" )
)
process.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducer" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originHalfLength = cms.double( 15.9 ),
      originZPos = cms.double( 0.0 ),
      originYPos = cms.double( 0.0 ),
      ptMin = cms.double( 0.9 ),
      originXPos = cms.double( 0.0 ),
      originRadius = cms.double( 0.2 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    ),
    SeedingLayers = cms.string( "hltPixelLayerTriplets" )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelTracksForHighMult = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducer" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originHalfLength = cms.double( 10.5 ),
      originRadius = cms.double( 0.5 ),
      originYPos = cms.double( 0.0 ),
      ptMin = cms.double( 0.4 ),
      originXPos = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelTracksForMinBias = cms.EDProducer( "PixelTrackProducer",
  useFilterWithES = cms.bool( False ),
  RegionFactoryPSet = cms.PSet(
    ComponentName = cms.string( "GlobalRegionProducer" ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      originHalfLength = cms.double( 30.0 ),
      originRadius = cms.double( 0.5 ),
      originYPos = cms.double( 0.0 ),
      ptMin = cms.double( 0.2 ),
      originXPos = cms.double( 0.0 ),
      originZPos = cms.double( 0.0 )
    )
  ),
  OrderedHitsFactoryPSet = cms.PSet(
    ComponentName = cms.string( "StandardHitTripletGenerator" ),
    SeedingLayers = cms.string( "hltPixelLayerTriplets" ),
    GeneratorPSet = cms.PSet(
      useBending = cms.bool( True ),
      useFixedPreFiltering = cms.bool( False ),
      phiPreFiltering = cms.double( 0.3 ),
      extraHitRPhitolerance = cms.double( 0.06 ),
      useMultScattering = cms.bool( True ),
      ComponentName = cms.string( "PixelTripletHLTGenerator" ),
      extraHitRZtolerance = cms.double( 0.06 ),
      maxElement = cms.uint32( 10000 )
    )
  ),
  FitterPSet = cms.PSet(
    ComponentName = cms.string( "PixelFitterByHelixProjections" ),
    TTRHBuilder = cms.string( "TTRHBuilderPixelOnly" )
  ),
  FilterPSet = cms.PSet(
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    tipMax = cms.double( 1.0 )
  ),
  CleanerPSet = cms.PSet(
    ComponentName = cms.string( "PixelTrackCleanerBySharedHits" )
  )
)
process.hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 1.0 ),
  TrackCollection = cms.InputTag( "hltPixelTracks" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltPixelVerticesForHighMult = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.05 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 0.2 ),
  TrackCollection = cms.InputTag( "hltPixelTracksForHighMult" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltPixelVerticesForMultiVertex = cms.EDProducer( "PixelVertexProducer",
  Verbosity = cms.int32( 0 ),
  Finder = cms.string( "DivisiveVertexFinder" ),
  UseError = cms.bool( True ),
  WtAverage = cms.bool( True ),
  ZOffset = cms.double( 5.0 ),
  ZSeparation = cms.double( 0.3 ),
  NTrkMin = cms.int32( 2 ),
  PtMin = cms.double( 0.5 ),
  TrackCollection = cms.InputTag( "hltPixelTracks" ),
  beamSpot = cms.InputTag( "hltOfflineBeamSpot" ),
  Method2 = cms.bool( True )
)
process.hltPreActivityCSC = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreActivityDT = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreActivityDTTuned = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreActivityEcalSC17 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreActivityEcalSC7 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaDTErrors = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalEta8E29 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalPhiSym = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreAlCaEcalPi08E29 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreBTagMuDiJet10U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreBTagMuDiJet20U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreBTagMuDiJet20UMu5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDQM = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDQMSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "HLT_Activity_CSC / 10", "HLT_Activity_DT / 10", "HLT_Activity_DT_Tuned / 10", "HLT_Activity_Ecal_SC17 / 10", "HLT_Activity_Ecal_SC7 / 10", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_Calibration / 10", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalCalibration / 0", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalCalibration / 0", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreDiJetAve100U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDiJetAve15U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDiJetAve30U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDiJetAve50U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDiJetAve70U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleEle15SWL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleEle4SWeeResL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleIsoTau15Trk5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleJet15UForwardBackward = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleJet25UForwardBackward = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleMu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleMu0Quark = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleMu0QuarkLS = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleMu3 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleMu5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoubleOneLegIsoTau15Trk5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoublePhoton17L1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreDoublePhoton5CEPL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEcalCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEcalOnlySumEt160 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle10MET45 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle10SWL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle12SWEleIdL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle12SWTigherEleIdIsolL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle12SWTighterEleIdL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17SWL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17SWTigherEleIdIsolL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17SWTightEleIdIsolL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17SWTightEleIdL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17SWTighterEleIdL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17TightCaloEleIdEle8HEL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle17TightCaloEleIdSC8HEL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle27SWTightCaloEleIdTrackL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreEle32SWTightCaloEleIdTrackL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExclDiJet30UHFAND = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExclDiJet30UHFOR = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExpress = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreExpressSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "HLT_DoubleMu3_v2", "HLT_Jet140U_v1", "HLT_L1Tech_BSC_minBias_OR / 2", "HLT_MET100_v2", "HLT_Mu15_v1", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_TrackerCosmics / 30", "HLT_ZeroBias / 10" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreFEDIntegrity = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreGlobalRunHPDNoise = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTDQM = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTDQMResults = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTDQMResultsSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "HLT_*" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHLTDQMSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "AlCa_EcalEta / 100", "AlCa_EcalPhiSym / 100", "AlCa_EcalPi0 / 100", "AlCa_RPCMuonNoHits / 100", "AlCa_RPCMuonNoTriggers / 100", "AlCa_RPCMuonNormalisation / 100", "HLT_Activity_CSC / 10", "HLT_Activity_DT / 10", "HLT_Activity_DT_Tuned / 10", "HLT_Activity_Ecal_SC17 / 10", "HLT_Activity_Ecal_SC7 / 10", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHLTMON = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHLTMONSmart = cms.HLTFilter( "TriggerResultsFilter",
  triggerConditions = cms.vstring( "AlCa_EcalEta / 250", "AlCa_EcalPhiSym / 250", "AlCa_EcalPi0 / 250", "AlCa_RPCMuonNoHits / 250", "AlCa_RPCMuonNoTriggers / 250", "AlCa_RPCMuonNormalisation / 250", "HLT_Activity_CSC", "HLT_Activity_DT", "HLT_Activity_DT_Tuned", "HLT_Activity_Ecal_SC17", "HLT_Activity_Ecal_SC7", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX / 100", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" ),
  hltResults = cms.InputTag( "TriggerResults" ),
  l1tResults = cms.InputTag( "" ),
  l1tIgnoreMask = cms.bool( False ),
  daqPartitions = cms.uint32( 1 ),
  throw = cms.bool( True ),
  l1techIgnorePrescales = cms.bool( False )
)
process.hltPreHT100U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT120 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT140U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT140UEta3 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT160U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT200U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHT50U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHcalCalibration = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHcalNZS8E29 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHcalPhiSym = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreHighMultiplicityBSC = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoMu11 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoMu9 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoTrackHB8E29 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreIsoTrackHE8E29 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet100U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet140U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet15U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet15UHcalNoiseFiltered = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet30U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet50U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreJet70U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BPTXMinusOnly = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BPTXPlusOnly = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1BptxXORBscMinBiasOR = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1DoubleMuOpen = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1ETT100 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1ETT140 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1HFTech = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1Jet10U_BPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1Jet6U_BPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1MET20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1Mu20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1Mu7 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1MuOpenDT = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1MuOpen_AntiBPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1MuOpen_BPTX = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleEG2 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1SingleEG8 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechBSChalo = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechBSChalo_forPhysicsBackground = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechBSCminBias = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechBSCminBiasOR = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL1TechRPCTTURBst1collisions = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2DoubleMu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2DoubleMu20NoVertex = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2Mu0NoVertex = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2Mu30 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreL2Mu7 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreLogMonitor = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET100 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET45 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET45HT100U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET45HT120U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET65 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMET80 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMinBiasPixelSingleTrack = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu0TkMu0Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu0TkMu0JpsiSeagull = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu11 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu13 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu15 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu20NoVertex = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu3 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu3TkMu0Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu3Track3Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu3Track5Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Ele5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Ele9 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5HT50U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5HT70U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Jet35U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Jet50U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5L2Mu0 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5MET45 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Photon11CleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5TkMu0Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu5Track0Jpsi = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu7 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMu9 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMultiVertex6 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreMultiVertex8 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreNanoDST = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePho30IsolEBOnlyL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePho35IsolL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton100NoHECleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton10L1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton15CleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton20CleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton20L1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton30CleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton50HECleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton50L1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePhoton70NoHECleanedL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity100 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity70 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPrePixelTracksMultiplicity85 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreQuadJet15U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreQuadJet20U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreQuadJet25U = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCBarrelCosmics = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNoHits = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNoTriggers = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRPCMuonNorma = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreRandom = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreSingleIsoTau20Trk15MET20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreSingleIsoTau20Trk5MET20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreSingleIsoTau30L120or30Trk5 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreSingleIsoTau30Trk5MET20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreSinglePhoton17SC17HEL1R = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreStoppedHSCP20 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreStoppedHSCP35 = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreTechTrigHCALNoise = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreTrackerCosmics = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreZeroBias = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltPreZeroBiasPixelSingleTrack = cms.HLTFilter( "HLTPrescaler",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" )
)
process.hltRPCFEDIntegrity = cms.EDAnalyzer( "RPCFEDIntegrity",
  RPCRawCountsInputTag = cms.untracked.InputTag( "hltMuonRPCDigis" ),
  RPCPrefixDir = cms.untracked.string( "RPC/FEDIntegrity" ),
  MergeRuns = cms.untracked.bool( False ),
  MinimumFEDID = cms.untracked.int32( 790 ),
  MaximumFEDID = cms.untracked.int32( 792 )
)
process.hltRPCFilter = cms.HLTFilter( "HLTRPCFilter",
  rangestrips = cms.untracked.double( 1.0 ),
  rpcRecHits = cms.InputTag( "hltRpcRecHits" ),
  rpcDTPoints = cms.InputTag( "hltRPCPointProducer:RPCDTExtrapolatedPoints" ),
  rpcCSCPoints = cms.InputTag( "hltRPCPointProducer:RPCCSCExtrapolatedPoints" )
)
process.hltRPCMuonNoTriggersL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sAlCaRPC" ),
  MaxEta = cms.double( 1.6 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32( 6 )
)
process.hltRPCMuonNormaL1Filtered0 = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sAlCaRPC" ),
  MaxEta = cms.double( 1.6 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( True ),
  SelectQualities = cms.vint32(  )
)
process.hltRPCPointProducer = cms.EDProducer( "RPCPointProducer",
  cscSegments = cms.InputTag( "hltCscSegments" ),
  dt4DSegments = cms.InputTag( "hltDt4DSegments" ),
  tracks = cms.InputTag( "" ),
  debug = cms.untracked.bool( False ),
  incldt = cms.untracked.bool( True ),
  inclcsc = cms.untracked.bool( True ),
  incltrack = cms.untracked.bool( False ),
  MinCosAng = cms.untracked.double( 0.95 ),
  MaxD = cms.untracked.double( 80.0 ),
  MaxDrb4 = cms.untracked.double( 150.0 ),
  ExtrapolatedRegion = cms.untracked.double( 0.5 ),
  TrackTransformer = cms.PSet(

  )
)
process.hltRandomEventsFilter = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 3 )
)
process.hltRecoEcalSuperClusterActivityCandidate = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
  scHybridBarrelProducer = cms.InputTag( "hltCorrectedHybridSuperClustersActivity" ),
  scIslandEndcapProducer = cms.InputTag( "hltCorrectedMulti5x5SuperClustersWithPreshowerActivity" ),
  recoEcalCandidateCollection = cms.string( "" )
)
process.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
  rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
  recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
  maskSource = cms.string( "File" ),
  maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
  deadSource = cms.string( "File" ),
  deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
  recAlgoConfig = cms.PSet(

  )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
  scalersInputTag = cms.InputTag( "source" )
)
process.hltSelector4JetsU = cms.EDFilter( "LargestEtCaloJetSelector",
  src = cms.InputTag( "hltMCJetCorJetIcone5HF07" ),
  filter = cms.bool( False ),
  maxNumber = cms.uint32( 4 )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
  src = cms.InputTag( "hltSiPixelDigis" ),
  maxNumberOfClusters = cms.int32( 10000 ),
  payloadType = cms.string( "HLT" ),
  ClusterMode = cms.untracked.string( "PixelThresholdClusterizer" ),
  ChannelThreshold = cms.int32( 1000 ),
  SeedThreshold = cms.int32( 1000 ),
  ClusterThreshold = cms.double( 4000.0 ),
  VCaltoElectronGain = cms.int32( 65 ),
  VCaltoElectronOffset = cms.int32( -414 ),
  MissCalibrate = cms.untracked.bool( True ),
  SplitClusters = cms.bool( False )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
  IncludeErrors = cms.bool( False ),
  UseCablingTree = cms.untracked.bool( True ),
  Timing = cms.untracked.bool( False ),
  InputLabel = cms.InputTag( "source" )
)
process.hltSiPixelDigisWithErrors = cms.EDProducer( "SiPixelRawToDigi",
  IncludeErrors = cms.bool( False ),
  UseCablingTree = cms.untracked.bool( True ),
  Timing = cms.untracked.bool( False ),
  InputLabel = cms.InputTag( "source" )
)
process.hltSiPixelHLTSource = cms.EDAnalyzer( "SiPixelHLTSource",
  RawInput = cms.InputTag( "source" ),
  ErrorInput = cms.InputTag( "hltSiPixelDigisWithErrors" ),
  saveFile = cms.untracked.bool( False ),
  slowDown = cms.untracked.bool( False ),
  DirName = cms.untracked.string( "Pixel/FEDIntegrity" ),
  outputFile = cms.string( "Pixel_DQM_HLT.root" )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
  src = cms.InputTag( "hltSiPixelClusters" ),
  VerboseLevel = cms.untracked.int32( 0 ),
  CPE = cms.string( "PixelCPEGeneric" )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerSiStripRefGetterProducer",
  InputModuleLabel = cms.InputTag( "hltSiStripRawToClustersFacility" ),
  measurementTrackerName = cms.string( "hltMeasurementTracker" )
)
process.hltSiStripFEDCheck = cms.EDAnalyzer( "SiStripFEDCheckPlugin",
  RawDataTag = cms.InputTag( "source" ),
  DirName = cms.untracked.string( "SiStrip/FEDIntegrity" ),
  PrintDebugMessages = cms.untracked.bool( False ),
  WriteDQMStore = cms.untracked.bool( False ),
  HistogramUpdateFrequency = cms.untracked.uint32( 1000 ),
  DoPayloadChecks = cms.untracked.bool( False ),
  CheckChannelLengths = cms.untracked.bool( False ),
  CheckChannelPacketCodes = cms.untracked.bool( False ),
  CheckFELengths = cms.untracked.bool( False ),
  CheckChannelStatus = cms.untracked.bool( False )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripRawToClusters",
  ProductLabel = cms.InputTag( "source" ),
  Clusterizer = cms.PSet(
    ChannelThreshold = cms.double( 2.0 ),
    MaxSequentialBad = cms.uint32( 1 ),
    Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
    MaxSequentialHoles = cms.uint32( 0 ),
    MaxAdjacentBad = cms.uint32( 0 ),
    QualityLabel = cms.string( "" ),
    SeedThreshold = cms.double( 3.0 ),
    ClusterThreshold = cms.double( 5.0 )
  ),
  Algorithms = cms.PSet(
    SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
    CommonModeNoiseSubtractionMode = cms.string( "Median" ),
    PedestalSubtractionFedMode = cms.bool( True ),
    TruncateInSuppressor = cms.bool( True )
  )
)
process.hltSimple3x3Clusters = cms.EDProducer( "EgammaHLTNxNClusterProducer",
  doBarrel = cms.bool( True ),
  doEndcaps = cms.bool( True ),
  barrelHitProducer = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEB" ),
  endcapHitProducer = cms.InputTag( "hltEcalRegionalPi0EtaRecHit:EcalRecHitsEE" ),
  clusEtaSize = cms.int32( 3 ),
  clusPhiSize = cms.int32( 3 ),
  barrelClusterCollection = cms.string( "Simple3x3ClustersBarrel" ),
  endcapClusterCollection = cms.string( "Simple3x3ClustersEndcap" ),
  clusSeedThr = cms.double( 0.5 ),
  clusSeedThrEndCap = cms.double( 1.0 ),
  useRecoFlag = cms.bool( False ),
  flagLevelRecHitsToUse = cms.int32( 1 ),
  useDBStatus = cms.bool( True ),
  statusLevelRecHitsToUse = cms.int32( 1 ),
  posCalc_logweight = cms.bool( True ),
  posCalc_t0_barl = cms.double( 7.4 ),
  posCalc_t0_endc = cms.double( 3.1 ),
  posCalc_t0_endcPresh = cms.double( 1.2 ),
  posCalc_w0 = cms.double( 4.2 ),
  posCalc_x0 = cms.double( 0.89 ),
  maxNumberofSeeds = cms.int32( 200 ),
  maxNumberofClusters = cms.int32( 30 ),
  debugLevel = cms.int32( 0 )
)
process.hltSingleL2Mu0L2PreFilteredNoVtx = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidatesNoVtx" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu0L1Filtered" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 0.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu0L1Filtered = cms.HLTFilter( "HLTMuonL1Filter",
  CandTag = cms.InputTag( "hltL1extraParticles" ),
  PreviousCandTag = cms.InputTag( "hltL1sL1SingleMu0" ),
  MaxEta = cms.double( 2.5 ),
  MinPt = cms.double( 0.0 ),
  MinN = cms.int32( 1 ),
  ExcludeSingleSegmentCSC = cms.bool( False ),
  CSCTFtag = cms.InputTag( "unused" ),
  SaveTag = cms.untracked.bool( False ),
  SelectQualities = cms.vint32(  )
)
process.hltSingleMu11L3Filtered11 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 11.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu13L3Filtered13 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 13.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu15L3Filtered15 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 15.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L2Filtered3 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu0L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu3L3Filtered3 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu3L2Filtered3" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 3.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu5EG5L2Filtered4 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu3EG5L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 4.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu5EG5L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu5EG5L2Filtered4" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu5L2Filtered4 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu3L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 4.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu5L3Filtered5 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu5L2Filtered4" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu7L2Filtered5 = cms.HLTFilter( "HLTMuonL2PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL1SingleMu5L1Filtered0" ),
  SeedMapTag = cms.InputTag( "hltL2Muons" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 9999.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 5.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltSingleMu7L3Filtered7 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMu7L2Filtered5" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 7.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMu9L3Filtered9 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 9.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( True )
)
process.hltSingleMuIsoL2IsoFiltered7 = cms.HLTFilter( "HLTMuonIsoFilter",
  CandTag = cms.InputTag( "hltL2MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltL2Mu7L2Filtered7" ),
  MinN = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( False ),
  DepTag = cms.VInputTag( "hltL2MuonIsolations" ),
  IsolatorPSet = cms.PSet(

  )
)
process.hltSingleMuIsoL3IsoFiltered11 = cms.HLTFilter( "HLTMuonIsoFilter",
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered11" ),
  MinN = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( True ),
  DepTag = cms.VInputTag( "hltL3MuonIsolations" ),
  IsolatorPSet = cms.PSet(

  )
)
process.hltSingleMuIsoL3IsoFiltered9 = cms.HLTFilter( "HLTMuonIsoFilter",
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuIsoL3PreFiltered9" ),
  MinN = cms.int32( 1 ),
  SaveTag = cms.untracked.bool( True ),
  DepTag = cms.VInputTag( "hltL3MuonIsolations" ),
  IsolatorPSet = cms.PSet(

  )
)
process.hltSingleMuIsoL3PreFiltered11 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 11.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltSingleMuIsoL3PreFiltered9 = cms.HLTFilter( "HLTMuonL3PreFilter",
  BeamSpotTag = cms.InputTag( "hltOfflineBeamSpot" ),
  CandTag = cms.InputTag( "hltL3MuonCandidates" ),
  PreviousCandTag = cms.InputTag( "hltSingleMuIsoL2IsoFiltered7" ),
  MinN = cms.int32( 1 ),
  MaxEta = cms.double( 2.5 ),
  MinNhits = cms.int32( 0 ),
  MaxDr = cms.double( 2.0 ),
  MaxDz = cms.double( 9999.0 ),
  MinPt = cms.double( 9.0 ),
  NSigmaPt = cms.double( 0.0 ),
  SaveTag = cms.untracked.bool( False )
)
process.hltStoppedHSCP1CaloJetEnergy20 = cms.HLTFilter( "HLT1CaloJetEnergy",
  inputTag = cms.InputTag( "hltStoppedHSCPIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  MinE = cms.double( 20.0 ),
  MaxEta = cms.double( 3.0 ),
  MinN = cms.int32( 1 )
)
process.hltStoppedHSCP1CaloJetEnergy35 = cms.HLTFilter( "HLT1CaloJetEnergy",
  inputTag = cms.InputTag( "hltStoppedHSCPIterativeCone5CaloJets" ),
  saveTag = cms.untracked.bool( True ),
  MinE = cms.double( 35.0 ),
  MaxEta = cms.double( 3.0 ),
  MinN = cms.int32( 1 )
)
process.hltStoppedHSCPHpdFilter = cms.HLTFilter( "HLTHPDFilter",
  inputTag = cms.InputTag( "hltHbhereco" ),
  energy = cms.double( -99.0 ),
  hpdSpikeEnergy = cms.double( 10.0 ),
  hpdSpikeIsolationEnergy = cms.double( 1.0 ),
  rbxSpikeEnergy = cms.double( 50.0 ),
  rbxSpikeUnbalance = cms.double( 0.2 )
)
process.hltStoppedHSCPIterativeCone5CaloJets = cms.EDProducer( "FastjetJetProducer",
  UseOnlyVertexTracks = cms.bool( False ),
  UseOnlyOnePV = cms.bool( False ),
  DzTrVtxMax = cms.double( 0.0 ),
  DxyTrVtxMax = cms.double( 0.0 ),
  MinVtxNdof = cms.int32( 5 ),
  MaxVtxZ = cms.double( 15.0 ),
  jetAlgorithm = cms.string( "IterativeCone" ),
  rParam = cms.double( 0.5 ),
  src = cms.InputTag( "hltStoppedHSCPTowerMakerForAll" ),
  srcPVs = cms.InputTag( "offlinePrimaryVertices" ),
  jetType = cms.string( "CaloJet" ),
  jetPtMin = cms.double( 1.0 ),
  inputEtMin = cms.double( 0.3 ),
  inputEMin = cms.double( 0.0 ),
  doPVCorrection = cms.bool( False ),
  doPUOffsetCorr = cms.bool( False ),
  nSigmaPU = cms.double( 1.0 ),
  radiusPU = cms.double( 0.5 ),
  Active_Area_Repeats = cms.int32( 5 ),
  GhostArea = cms.double( 0.01 ),
  Ghost_EtaMax = cms.double( 6.0 ),
  maxBadEcalCells = cms.uint32( 9999999 ),
  maxRecoveredEcalCells = cms.uint32( 9999999 ),
  maxProblematicEcalCells = cms.uint32( 9999999 ),
  maxBadHcalCells = cms.uint32( 9999999 ),
  maxRecoveredHcalCells = cms.uint32( 9999999 ),
  maxProblematicHcalCells = cms.uint32( 9999999 ),
  doAreaFastjet = cms.bool( False ),
  doRhoFastjet = cms.bool( False ),
  subtractorName = cms.string( "" )
)
process.hltStoppedHSCPTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "" ),
  hfInput = cms.InputTag( "" ),
  AllowMissingInputs = cms.bool( True ),
  HcalAcceptSeverityLevel = cms.uint32( 9 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( False ),
  HcalAcceptSeverityLevel = cms.uint32( 999 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRecHitAll:EcalRecHitsEB", "hltEcalRecHitAll:EcalRecHitsEE" )
)
process.hltTowerMakerForEcalBarrelOnly = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "" ),
  hoInput = cms.InputTag( "" ),
  hfInput = cms.InputTag( "" ),
  AllowMissingInputs = cms.bool( True ),
  HcalAcceptSeverityLevel = cms.uint32( 999 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRecHitAll:EcalRecHitsEB" )
)
process.hltTowerMakerForHcal = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0e-99 ),
  EEWeight = cms.double( 1.0e-99 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( True ),
  HcalAcceptSeverityLevel = cms.uint32( 999 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag(  )
)
process.hltTowerMakerForJets = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( False ),
  HcalAcceptSeverityLevel = cms.uint32( 999 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRegionalJetsRecHit:EcalRecHitsEB", "hltEcalRegionalJetsRecHit:EcalRecHitsEE" )
)
process.hltTowerMakerForMuons = cms.EDProducer( "CaloTowersCreator",
  EBThreshold = cms.double( 0.07 ),
  EEThreshold = cms.double( 0.3 ),
  UseEtEBTreshold = cms.bool( False ),
  UseEtEETreshold = cms.bool( False ),
  UseSymEBTreshold = cms.bool( False ),
  UseSymEETreshold = cms.bool( False ),
  HcalThreshold = cms.double( -1000.0 ),
  HBThreshold = cms.double( 0.7 ),
  HESThreshold = cms.double( 0.8 ),
  HEDThreshold = cms.double( 0.8 ),
  HOThreshold0 = cms.double( 3.5 ),
  HOThresholdPlus1 = cms.double( 3.5 ),
  HOThresholdMinus1 = cms.double( 3.5 ),
  HOThresholdPlus2 = cms.double( 3.5 ),
  HOThresholdMinus2 = cms.double( 3.5 ),
  HF1Threshold = cms.double( 0.5 ),
  HF2Threshold = cms.double( 0.85 ),
  EBWeight = cms.double( 1.0 ),
  EEWeight = cms.double( 1.0 ),
  HBWeight = cms.double( 1.0 ),
  HESWeight = cms.double( 1.0 ),
  HEDWeight = cms.double( 1.0 ),
  HOWeight = cms.double( 1.0e-99 ),
  HF1Weight = cms.double( 1.0 ),
  HF2Weight = cms.double( 1.0 ),
  EcutTower = cms.double( -1000.0 ),
  EBSumThreshold = cms.double( 0.2 ),
  EESumThreshold = cms.double( 0.45 ),
  UseHO = cms.bool( False ),
  MomConstrMethod = cms.int32( 1 ),
  MomHBDepth = cms.double( 0.2 ),
  MomHEDepth = cms.double( 0.4 ),
  MomEBDepth = cms.double( 0.3 ),
  MomEEDepth = cms.double( 0.0 ),
  hbheInput = cms.InputTag( "hltHbhereco" ),
  hoInput = cms.InputTag( "hltHoreco" ),
  hfInput = cms.InputTag( "hltHfreco" ),
  AllowMissingInputs = cms.bool( False ),
  HcalAcceptSeverityLevel = cms.uint32( 999 ),
  EcalAcceptSeverityLevel = cms.uint32( 3 ),
  UseHcalRecoveredHits = cms.bool( True ),
  UseEcalRecoveredHits = cms.bool( True ),
  EBGrid = cms.vdouble(  ),
  EBWeights = cms.vdouble(  ),
  EEGrid = cms.vdouble(  ),
  EEWeights = cms.vdouble(  ),
  HBGrid = cms.vdouble(  ),
  HBWeights = cms.vdouble(  ),
  HESGrid = cms.vdouble(  ),
  HESWeights = cms.vdouble(  ),
  HEDGrid = cms.vdouble(  ),
  HEDWeights = cms.vdouble(  ),
  HOGrid = cms.vdouble(  ),
  HOWeights = cms.vdouble(  ),
  HF1Grid = cms.vdouble(  ),
  HF1Weights = cms.vdouble(  ),
  HF2Grid = cms.vdouble(  ),
  HF2Weights = cms.vdouble(  ),
  ecalInputs = cms.VInputTag( "hltEcalRegionalMuonsRecHit:EcalRecHitsEB", "hltEcalRegionalMuonsRecHit:EcalRecHitsEE" )
)
process.hltTrackerCosmicsPattern = cms.HLTFilter( "HLTLevel1Pattern",
  L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
  triggerBit = cms.string( "L1Tech_RPC_TTU_pointing_Cosmics.v0" ),
  daqPartitions = cms.uint32( 1 ),
  ignoreL1Mask = cms.bool( False ),
  invert = cms.bool( False ),
  throw = cms.bool( True ),
  bunchCrossings = cms.vint32( -2, -1, 0, 1, 2 ),
  triggerPattern = cms.vint32( 1, 1, 1, 0, 0 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
  processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
  processName = cms.string( "@" )
)
process.hltTriggerType = cms.HLTFilter( "HLTTriggerTypeFilter",
  SelectedTriggerType = cms.int32( 1 )
)
process.hltVertexFilter6 = cms.HLTFilter( "HLTVertexFilter",
  inputTag = cms.InputTag( "hltPixelVerticesForMultiVertex" ),
  minNDoF = cms.double( 0.0 ),
  maxChi2 = cms.double( 99999.0 ),
  maxD0 = cms.double( 1.0 ),
  maxZ = cms.double( 15.0 ),
  minVertices = cms.uint32( 6 )
)
process.hltVertexFilter8 = cms.HLTFilter( "HLTVertexFilter",
  inputTag = cms.InputTag( "hltPixelVerticesForMultiVertex" ),
  minNDoF = cms.double( 0.0 ),
  maxChi2 = cms.double( 99999.0 ),
  maxD0 = cms.double( 1.0 ),
  maxZ = cms.double( 15.0 ),
  minVertices = cms.uint32( 8 )
)

process.hltOutputA = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_Activity_CSC", "HLT_Activity_DT", "HLT_Activity_DT_Tuned", "HLT_Activity_Ecal_SC17", "HLT_Activity_Ecal_SC7", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputExpress = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLT_DoubleMu3_v2", "HLT_Jet140U_v1", "HLT_L1Tech_BSC_minBias_OR", "HLT_MET100_v2", "HLT_Mu15_v1", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_TrackerCosmics", "HLT_ZeroBias" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputALCAP0 = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta", "AlCa_EcalPi0" )
  ),
  outputCommands = cms.untracked.vstring( "drop *", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputDQM = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "DQM_FEDIntegrity", "HLT_Activity_CSC", "HLT_Activity_DT", "HLT_Activity_DT_Tuned", "HLT_Activity_Ecal_SC17", "HLT_Activity_Ecal_SC7", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_Calibration", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalCalibration", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalCalibration", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltL1GtObjectMap_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQM = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta", "AlCa_EcalPhiSym", "AlCa_EcalPi0", "AlCa_RPCMuonNoHits", "AlCa_RPCMuonNoTriggers", "AlCa_RPCMuonNormalisation", "HLT_Activity_CSC", "HLT_Activity_DT", "HLT_Activity_DT_Tuned", "HLT_Activity_Ecal_SC17", "HLT_Activity_Ecal_SC7", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPhiSymStream_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep *_hltBLifetimeL25AssociatorStartupU_*_*", "keep *_hltBLifetimeL25BJetTagsStartupU_*_*", "keep *_hltBLifetimeL25JetsStartupU_*_*", "keep *_hltBLifetimeL25TagInfosStartupU_*_*", "keep *_hltBLifetimeL3AssociatorStartupU_*_*", "keep *_hltBLifetimeL3BJetTagsStartupU_*_*", "keep *_hltBLifetimeL3JetsStartupU_*_*", "keep *_hltBLifetimeL3TagInfosStartupU_*_*", "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*", "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL25JetsU_*_*", "keep *_hltBSoftMuonL25TagInfosU_*_*", "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL3TagInfosU_*_*", "keep *_hltCsc2DRecHits_*_*", "keep *_hltCscSegments_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*", "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*", "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltGtDigis_*_*", "keep *_hltHITCtfWithMaterialTracksHB8E29_*_*", "keep *_hltHITCtfWithMaterialTracksHE8E29_*_*", "keep *_hltHITIPTCorrectorHB8E29_*_*", "keep *_hltHITIPTCorrectorHE8E29_*_*", "keep *_hltHcalDigis_*_*", "keep *_hltIconeCentral1Regional_*_*", "keep *_hltIconeCentral2Regional_*_*", "keep *_hltIconeCentral3Regional_*_*", "keep *_hltIconeCentral4Regional_*_*", "keep *_hltIconeTau1Regional_*_*", "keep *_hltIconeTau2Regional_*_*", "keep *_hltIconeTau3Regional_*_*", "keep *_hltIconeTau4Regional_*_*", "keep *_hltIsolPixelTrackProdHB8E29_*_*", "keep *_hltIsolPixelTrackProdHE8E29_*_*", "keep *_hltIterativeCone5CaloJets_*_*", "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1IsoRecoEcalCandidate_*_*", "keep *_hltL1IsoSiStripElectronPixelSeeds_*_*", "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1IsolatedElectronHcalIsol_*_*", "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1NonIsoRecoEcalCandidate_*_*", "keep *_hltL1NonIsoSiStripElectronPixelSeeds_*_*", "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1NonIsolatedElectronHcalIsol_*_*", "keep *_hltL1extraParticles_*_*", "keep *_hltL1sDoubleLooseIsoTau15_*_*", "keep *_hltL1sSingleLooseIsoTau20_*_*", "keep *_hltL25TauConeIsolation_*_*", "keep *_hltL25TauCtfWithMaterialTracks_*_*", "keep *_hltL25TauJetTracksAssociator_*_*", "keep *_hltL25TauLeadingTrackPtCutSelector_*_*", "keep *_hltL2MuonCandidates_*_*", "keep *_hltL2MuonIsolations_*_*", "keep *_hltL2MuonSeeds_*_*", "keep *_hltL2Muons_*_*", "keep *_hltL2TauJets_*_*", "keep *_hltL2TauNarrowConeIsolationProducer_*_*", "keep *_hltL2TauRelaxingIsolationSelector_*_*", "keep *_hltL3MuonCandidates_*_*", "keep *_hltL3MuonIsolations_*_*", "keep *_hltL3MuonsIOHit_*_*", "keep *_hltL3MuonsLinksCombination_*_*", "keep *_hltL3MuonsOIHit_*_*", "keep *_hltL3MuonsOIState_*_*", "keep *_hltL3Muons_*_*", "keep *_hltL3TauConeIsolation_*_*", "keep *_hltL3TauCtfWithMaterialTracks_*_*", "keep *_hltL3TauIsolationSelector_*_*", "keep *_hltL3TauJetTracksAssociator_*_*", "keep *_hltL3TkFromL2OICombination_*_*", "keep *_hltL3TkTracksFromL2IOHit_*_*", "keep *_hltL3TkTracksFromL2OIHit_*_*", "keep *_hltL3TkTracksFromL2OIState_*_*", "keep *_hltL3TrackCandidateFromL2IOHit_*_*", "keep *_hltL3TrackCandidateFromL2OIHit_*_*", "keep *_hltL3TrackCandidateFromL2OIState_*_*", "keep *_hltL3TrajSeedIOHit_*_*", "keep *_hltL3TrajSeedOIHit_*_*", "keep *_hltL3TrajSeedOIState_*_*", "keep *_hltL3TrajectorySeed_*_*", "keep *_hltMCJetCorJetIcone5HF07_*_*", "keep *_hltMet_*_*", "keep *_hltMuTrackJpsiCtfTrackCands_*_*", "keep *_hltMuTrackJpsiPixelTrackCands_*_*", "keep *_hltMuonCSCDigis_*_*", "keep *_hltMuonRPCDigis_*_*", "keep *_hltOfflineBeamSpot_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*", "keep *_hltPixelTracks_*_*", "keep *_hltRpcRecHits_*_*", "keep *_hltSiPixelClusters_*_*", "keep *_hltSiStripRawToClustersFacility_*_*", "keep *_hltTowerMakerForMuons_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputHLTDQMResults = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLTriggerFinalPath" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep LumiScalerss_*_*_*", "keep edmTriggerResults_*_*_*" )
)
process.hltOutputHLTMON = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "AlCa_EcalEta", "AlCa_EcalPhiSym", "AlCa_EcalPi0", "AlCa_RPCMuonNoHits", "AlCa_RPCMuonNoTriggers", "AlCa_RPCMuonNormalisation", "HLT_Activity_CSC", "HLT_Activity_DT", "HLT_Activity_DT_Tuned", "HLT_Activity_Ecal_SC17", "HLT_Activity_Ecal_SC7", "HLT_BTagMu_DiJet10U_v1", "HLT_BTagMu_DiJet20U_Mu5_v1", "HLT_BTagMu_DiJet20U_v1", "HLT_DTErrors", "HLT_DiJetAve100U_v1", "HLT_DiJetAve15U", "HLT_DiJetAve30U", "HLT_DiJetAve50U", "HLT_DiJetAve70U_v2", "HLT_DoubleEle15_SW_L1R_v1", "HLT_DoubleEle4_SW_eeRes_L1R", "HLT_DoubleIsoTau15_OneLeg_Trk5", "HLT_DoubleIsoTau15_Trk5", "HLT_DoubleJet15U_ForwardBackward", "HLT_DoubleJet25U_ForwardBackward", "HLT_DoubleMu0_Quarkonium_LS_v1", "HLT_DoubleMu0_Quarkonium_v1", "HLT_DoubleMu3_v2", "HLT_DoubleMu5_v1", "HLT_DoublePhoton17_L1R", "HLT_DoublePhoton5_CEP_L1R", "HLT_EcalOnly_SumEt160_v2", "HLT_Ele10_MET45_v1", "HLT_Ele10_SW_L1R", "HLT_Ele12_SW_TightEleId_L1R", "HLT_Ele12_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele12_SW_TighterEleId_L1R_v1", "HLT_Ele17_SW_L1R", "HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1", "HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1", "HLT_Ele17_SW_TightEleIdIsol_L1R_v1", "HLT_Ele17_SW_TightEleId_L1R", "HLT_Ele17_SW_TighterEleIdIsol_L1R_v1", "HLT_Ele17_SW_TighterEleId_L1R_v1", "HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1", "HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1", "HLT_ExclDiJet30U_HFAND_v1", "HLT_ExclDiJet30U_HFOR_v1", "HLT_GlobalRunHPDNoise", "HLT_HT100U", "HLT_HT120U", "HLT_HT140U", "HLT_HT140U_Eta3_v1", "HLT_HT160U_v1", "HLT_HT200U_v1", "HLT_HT50U_v1", "HLT_HcalNZS", "HLT_HcalPhiSym", "HLT_IsoMu11_v1", "HLT_IsoMu9", "HLT_IsoTrackHB_v2", "HLT_IsoTrackHE_v2", "HLT_Jet100U_v2", "HLT_Jet140U_v1", "HLT_Jet15U", "HLT_Jet15U_HcalNoiseFiltered", "HLT_Jet30U", "HLT_Jet50U", "HLT_Jet70U_v2", "HLT_L1DoubleMuOpen", "HLT_L1ETT100", "HLT_L1ETT140_v1", "HLT_L1Jet10U", "HLT_L1Jet6U", "HLT_L1MET20", "HLT_L1Mu20", "HLT_L1Mu7_v1", "HLT_L1MuOpen", "HLT_L1MuOpen_AntiBPTX", "HLT_L1MuOpen_DT", "HLT_L1SingleEG2", "HLT_L1SingleEG8", "HLT_L1Tech_BSC_HighMultiplicity", "HLT_L1Tech_BSC_halo", "HLT_L1Tech_BSC_halo_forPhysicsBackground", "HLT_L1Tech_BSC_minBias", "HLT_L1Tech_BSC_minBias_OR", "HLT_L1Tech_HCAL_HF", "HLT_L1Tech_RPC_TTU_RBst1_collisions", "HLT_L1_BPTX", "HLT_L1_BPTX_MinusOnly", "HLT_L1_BPTX_PlusOnly", "HLT_L1_BptxXOR_BscMinBiasOR", "HLT_L2DoubleMu0", "HLT_L2DoubleMu20_NoVertex_v1", "HLT_L2Mu0_NoVertex", "HLT_L2Mu30_v1", "HLT_L2Mu7_v1", "HLT_LogMonitor", "HLT_MET100_v2", "HLT_MET45", "HLT_MET45_HT100U_v1", "HLT_MET45_HT120U_v1", "HLT_MET65", "HLT_MET80_v1", "HLT_MinBiasPixel_SingleTrack", "HLT_Mu0_TkMu0_OST_Jpsi", "HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1", "HLT_Mu11", "HLT_Mu13_v1", "HLT_Mu15_v1", "HLT_Mu20_NoVertex", "HLT_Mu3", "HLT_Mu3_TkMu0_OST_Jpsi", "HLT_Mu3_Track3_Jpsi", "HLT_Mu3_Track5_Jpsi_v1", "HLT_Mu5", "HLT_Mu5_Ele5_v1", "HLT_Mu5_Ele9_v1", "HLT_Mu5_HT50U_v1", "HLT_Mu5_HT70U_v1", "HLT_Mu5_Jet35U_v1", "HLT_Mu5_Jet50U_v2", "HLT_Mu5_L2Mu0", "HLT_Mu5_MET45_v1", "HLT_Mu5_Photon11_Cleaned_L1R_v1", "HLT_Mu5_TkMu0_OST_Jpsi", "HLT_Mu5_Track0_Jpsi", "HLT_Mu7", "HLT_Mu9", "HLT_MultiVertex6", "HLT_MultiVertex8_L1ETT60", "HLT_Photon100_NoHE_Cleaned_L1R_v1", "HLT_Photon10_Cleaned_L1R", "HLT_Photon15_Cleaned_L1R", "HLT_Photon17_SC17HE_L1R_v1", "HLT_Photon20_Cleaned_L1R", "HLT_Photon20_NoHE_L1R", "HLT_Photon30_Cleaned_L1R", "HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1", "HLT_Photon35_Isol_Cleaned_L1R_v1", "HLT_Photon50_Cleaned_L1R_v1", "HLT_Photon50_NoHE_L1R", "HLT_Photon70_NoHE_Cleaned_L1R_v1", "HLT_PixelTracks_Multiplicity100", "HLT_PixelTracks_Multiplicity70", "HLT_PixelTracks_Multiplicity85", "HLT_QuadJet15U_v2", "HLT_QuadJet20U_v2", "HLT_QuadJet25U_v2", "HLT_RPCBarrelCosmics", "HLT_Random", "HLT_SingleIsoTau20_Trk15_MET20", "HLT_SingleIsoTau20_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_MET20", "HLT_SingleIsoTau30_Trk5_v2", "HLT_StoppedHSCP20_v3", "HLT_StoppedHSCP35_v3", "HLT_TechTrigHCALNoise", "HLT_TrackerCosmics", "HLT_ZeroBias", "HLT_ZeroBiasPixel_SingleTrack" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltAlCaEtaRecHitsFilter_*_*", "keep *_hltAlCaPi0RecHitsFilter_*_*", "keep *_hltBLifetimeL25AssociatorStartupU_*_*", "keep *_hltBLifetimeL25BJetTagsStartupU_*_*", "keep *_hltBLifetimeL25JetsStartupU_*_*", "keep *_hltBLifetimeL25TagInfosStartupU_*_*", "keep *_hltBLifetimeL3AssociatorStartupU_*_*", "keep *_hltBLifetimeL3BJetTagsStartupU_*_*", "keep *_hltBLifetimeL3JetsStartupU_*_*", "keep *_hltBLifetimeL3TagInfosStartupU_*_*", "keep *_hltBLifetimeRegionalCtfWithMaterialTracksStartupU_*_*", "keep *_hltBSoftMuonL25BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL25JetsU_*_*", "keep *_hltBSoftMuonL25TagInfosU_*_*", "keep *_hltBSoftMuonL3BJetTagsUByDR_*_*", "keep *_hltBSoftMuonL3BJetTagsUByPt_*_*", "keep *_hltBSoftMuonL3TagInfosU_*_*", "keep *_hltCkfL1IsoLargeWindowTrackCandidates_*_*", "keep *_hltCkfL1NonIsoLargeWindowTrackCandidates_*_*", "keep *_hltCorrectedHybridSuperClustersL1Isolated_*_*", "keep *_hltCorrectedHybridSuperClustersL1NonIsolated_*_*", "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated_*_*", "keep *_hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated_*_*", "keep *_hltCscSegments_*_*", "keep *_hltCtfL1IsoLargeWindowWithMaterialTracks_*_*", "keep *_hltCtfL1NonIsoLargeWindowWithMaterialTracks_*_*", "keep *_hltDt1DRecHits_*_*", "keep *_hltDt4DSegments_*_*", "keep *_hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EcalIsolationDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EcalIsolationSingleLooseIsoTau20_*_*", "keep *_hltFilterL2EtCutDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL2EtCutDoubleLooseIsoTau15_*_*", "keep *_hltFilterL2EtCutSingleIsoTau30Trk5MET20_*_*", "keep *_hltFilterL2EtCutSingleLooseIsoTau20_*_*", "keep *_hltFilterL3TrackIsolationDoubleIsoTau15Trk5_*_*", "keep *_hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20_*_*", "keep *_hltGctDigis_*_*", "keep *_hltGtDigis_*_*", "keep *_hltHoreco_*_*", "keep *_hltIconeCentral1Regional_*_*", "keep *_hltIconeCentral2Regional_*_*", "keep *_hltIconeCentral3Regional_*_*", "keep *_hltIconeCentral4Regional_*_*", "keep *_hltIconeTau1Regional_*_*", "keep *_hltIconeTau2Regional_*_*", "keep *_hltIconeTau3Regional_*_*", "keep *_hltIconeTau4Regional_*_*", "keep *_hltL1GtObjectMap_*_*", "keep *_hltL1IsoEgammaRegionalCTFFinalFitWithMaterial_*_*", "keep *_hltL1IsoEgammaRegionalCkfTrackCandidates_*_*", "keep *_hltL1IsoEgammaRegionalPixelSeedGenerator_*_*", "keep *_hltL1IsoHLTClusterShape_*_*", "keep *_hltL1IsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1IsoPhotonHollowTrackIsol_*_*", "keep *_hltL1IsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1IsolatedPhotonEcalIsol_*_*", "keep *_hltL1IsolatedPhotonHcalIsol_*_*", "keep *_hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial_*_*", "keep *_hltL1NonIsoEgammaRegionalCkfTrackCandidates_*_*", "keep *_hltL1NonIsoEgammaRegionalPixelSeedGenerator_*_*", "keep *_hltL1NonIsoHLTClusterShape_*_*", "keep *_hltL1NonIsoLargeWindowElectronPixelSeeds_*_*", "keep *_hltL1NonIsoPhotonHollowTrackIsol_*_*", "keep *_hltL1NonIsoStartUpElectronPixelSeeds_*_*", "keep *_hltL1NonIsolatedPhotonEcalIsol_*_*", "keep *_hltL1NonIsolatedPhotonHcalIsol_*_*", "keep *_hltL1extraParticles_*_*", "keep *_hltL1sDoubleLooseIsoTau15_*_*", "keep *_hltL1sSingleLooseIsoTau20_*_*", "keep *_hltL25TauConeIsolation_*_*", "keep *_hltL25TauCtfWithMaterialTracks_*_*", "keep *_hltL25TauJetTracksAssociator_*_*", "keep *_hltL25TauLeadingTrackPtCutSelector_*_*", "keep *_hltL2MuonCandidatesNoVtx_*_*", "keep *_hltL2MuonCandidates_*_*", "keep *_hltL2MuonIsolations_*_*", "keep *_hltL2MuonSeeds_*_*", "keep *_hltL2Muons_*_*", "keep *_hltL2TauJets_*_*", "keep *_hltL2TauNarrowConeIsolationProducer_*_*", "keep *_hltL2TauRelaxingIsolationSelector_*_*", "keep *_hltL3MuonCandidatesNoVtx_*_*", "keep *_hltL3MuonCandidates_*_*", "keep *_hltL3MuonIsolations_*_*", "keep *_hltL3MuonsIOHit_*_*", "keep *_hltL3MuonsLinksCombination_*_*", "keep *_hltL3MuonsNoVtx_*_*", "keep *_hltL3MuonsOIHit_*_*", "keep *_hltL3MuonsOIState_*_*", "keep *_hltL3Muons_*_*", "keep *_hltL3TauConeIsolation_*_*", "keep *_hltL3TauCtfWithMaterialTracks_*_*", "keep *_hltL3TauIsolationSelector_*_*", "keep *_hltL3TauJetTracksAssociator_*_*", "keep *_hltL3TkFromL2OICombination_*_*", "keep *_hltL3TkTracksFromL2IOHit_*_*", "keep *_hltL3TkTracksFromL2OIHit_*_*", "keep *_hltL3TkTracksFromL2OIState_*_*", "keep *_hltL3TkTracksFromL2_*_*", "keep *_hltL3TrackCandidateFromL2IOHit_*_*", "keep *_hltL3TrackCandidateFromL2OIHit_*_*", "keep *_hltL3TrackCandidateFromL2OIState_*_*", "keep *_hltL3TrackCandidateFromL2_*_*", "keep *_hltL3TrajSeedIOHit_*_*", "keep *_hltL3TrajSeedOIHit_*_*", "keep *_hltL3TrajSeedOIState_*_*", "keep *_hltL3TrajectorySeedNoVtx_*_*", "keep *_hltL3TrajectorySeed_*_*", "keep *_hltMet_*_*", "keep *_hltMuTrackJpsiCtfTrackCands_*_*", "keep *_hltMuTrackJpsiCtfTracks_*_*", "keep *_hltMuTrackJpsiPixelTrackCands_*_*", "keep *_hltMuTrackJpsiPixelTrackSelector_*_*", "keep *_hltMuTrackJpsiTrackSeeds_*_*", "keep *_hltMuonRPCDigis_*_*", "keep *_hltOfflineBeamSpot_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1Iso_*_*", "keep *_hltPixelMatchLargeWindowElectronsL1NonIso_*_*", "keep *_hltPixelTracks_*_*", "keep *_hltPixelVertices_*_*", "keep *_hltRpcRecHits_*_*", "keep *_hltSiPixelRecHits_*_*", "keep *_hltSiStripClusters_*_*", "keep *_hltSiStripRawToClustersFacility_*_*", "keep *_hltTowerMakerForAll_*_*", "keep *_hltTowerMakerForMuons_*_*", "keep FEDRawDataCollection_rawDataCollector_*_*", "keep FEDRawDataCollection_source_*_*", "keep SiPixelClusteredmNewDetSetVector_hltSiPixelClusters_*_*", "keep edmTriggerResults_*_*_*", "keep triggerTriggerEventWithRefs_*_*_*", "keep triggerTriggerEvent_*_*_*" )
)
process.hltOutputNanoDST = cms.OutputModule( "ShmStreamConsumer",
  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring( "HLTriggerFinalPath" )
  ),
  outputCommands = cms.untracked.vstring( "drop *_hlt*_*_*", "keep *_hltFEDSelector_*_*", "keep L1GlobalTriggerReadoutRecord_hltGtDigis_*_*", "keep L1MuGMTReadoutCollection_hltGtDigis_*_*", "keep edmTriggerResults_*_*_*" )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot + process.hltOfflineBeamSpot )
process.HLTBeginSequenceBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )
process.HLTEcalActivitySequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRegionalESRestFEDs + process.hltEcalRecHitAll + process.hltESRecHitAll + process.hltHybridSuperClustersActivity + process.hltCorrectedHybridSuperClustersActivity + process.hltMulti5x5BasicClustersActivity + process.hltMulti5x5SuperClustersActivity + process.hltMulti5x5SuperClustersWithPreshowerActivity + process.hltCorrectedMulti5x5SuperClustersWithPreshowerActivity + process.hltRecoEcalSuperClusterActivityCandidate + process.hltEcalActivitySuperClusterWrapper )
process.HLTDoLocalHcalSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco )
process.HLTDoCaloSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.HLTDoLocalHcalSequence + process.hltTowerMakerForAll )
process.HLTRecoJetSequenceU = cms.Sequence( process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltMCJetCorJetIcone5HF07 )
process.HLTHcalNoiseSequence = cms.Sequence( process.hltHcalNoiseInfoProducer + process.hltHcalMETNoiseFilter )
process.HLTDoRegionalJetEcalSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalJetsFEDs + process.hltEcalRegionalJetsRecHit )
process.HLTRecoJetRegionalSequence = cms.Sequence( process.HLTDoRegionalJetEcalSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForJets + process.hltIterativeCone5CaloJetsRegional + process.hltMCJetCorJetIcone5Regional )
process.HLTRecoMETSequence = cms.Sequence( process.HLTDoCaloSequence + process.hltMet )
process.HLTDoJet20UHTRecoSequence = cms.Sequence( process.hltJet20UHt )
process.HLTBeginSequenceAntiBPTX = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.hltBPTXAntiCoincidence + process.HLTBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTmuonlocalrecoSequence = cms.Sequence( process.hltMuonDTDigis + process.hltDt1DRecHits + process.hltDt4DSegments + process.hltMuonCSCDigis + process.hltCsc2DRecHits + process.hltCscSegments + process.hltMuonRPCDigis + process.hltRpcRecHits )
process.HLTL2muonrecoNocandSequence = cms.Sequence( process.HLTmuonlocalrecoSequence + process.hltL2MuonSeeds + process.hltL2Muons )
process.HLTL2muonrecoSequenceNoVtx = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidatesNoVtx )
process.HLTL2muonrecoSequence = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltL2MuonCandidates )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )
process.HLTL3muonTkCandidateSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajSeedOIState + process.hltL3TrackCandidateFromL2OIState + process.hltL3TkTracksFromL2OIState + process.hltL3MuonsOIState + process.hltL3TrajSeedOIHit + process.hltL3TrackCandidateFromL2OIHit + process.hltL3TkTracksFromL2OIHit + process.hltL3MuonsOIHit + process.hltL3TkFromL2OICombination + process.hltL3TrajSeedIOHit + process.hltL3TrackCandidateFromL2IOHit + process.hltL3TkTracksFromL2IOHit + process.hltL3MuonsIOHit + process.hltL3TrajectorySeed + process.hltL3TrackCandidateFromL2 )
process.HLTL3muonrecoNocandSequence = cms.Sequence( process.HLTL3muonTkCandidateSequence + process.hltL3TkTracksFromL2 + process.hltL3MuonsLinksCombination + process.hltL3Muons )
process.HLTL3muonrecoSequence = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltL3MuonCandidates )
process.HLTL2muonisorecoSequence = cms.Sequence( process.hltEcalRawToRecHitFacility + process.hltEcalRegionalMuonsFEDs + process.hltEcalRegionalMuonsRecHit + process.HLTDoLocalHcalSequence + process.hltTowerMakerForMuons + process.hltL2MuonIsolations )
process.HLTL3muonisorecoSequence = cms.Sequence( process.hltPixelTracks + process.hltL3MuonIsolations )
process.HLTL3muonTkCandidateSequenceNoVtx = cms.Sequence( process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL3TrajectorySeedNoVtx + process.hltL3TrackCandidateFromL2NoVtx )
process.HLTL3muonrecoNocandSequenceNoVtx = cms.Sequence( process.HLTL3muonTkCandidateSequenceNoVtx + process.hltL3TkTracksFromL2NoVtx + process.hltL3MuonsNoVtx )
process.HLTL3muonrecoSequenceNoVtx = cms.Sequence( process.HLTL3muonrecoNocandSequenceNoVtx + process.hltL3MuonCandidatesNoVtx )
process.HLTMuTrackJpsiPixelRecoSequence = cms.Sequence( process.HLTDoLocalPixelSequence + process.hltPixelTracks + process.hltMuTrackJpsiPixelTrackSelector + process.hltMuTrackJpsiPixelTrackCands )
process.HLTMuTrackJpsiTrackRecoSequence = cms.Sequence( process.HLTDoLocalStripSequence + process.hltMuTrackJpsiTrackSeeds + process.hltMuTrackJpsiCkfTrackCandidates + process.hltMuTrackJpsiCtfTracks + process.hltMuTrackJpsiCtfTrackCands )
process.HLTMuTkMuJpsiTkMuRecoSequence = cms.Sequence( process.hltMuTkMuJpsiTrackerMuons + process.hltMuTkMuJpsiTrackerMuonCands )
process.HLTDoRegionalEgammaEcalSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalEgammaFEDs + process.hltEcalRegionalEgammaRecHit + process.hltESRegionalEgammaRecHit )
process.HLTMulti5x5SuperClusterL1Isolated = cms.Sequence( process.hltMulti5x5BasicClustersL1Isolated + process.hltMulti5x5SuperClustersL1Isolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1Isolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1Isolated )
process.HLTL1IsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1Isolated + process.hltCorrectedHybridSuperClustersL1Isolated + process.HLTMulti5x5SuperClusterL1Isolated )
process.HLTMulti5x5SuperClusterL1NonIsolated = cms.Sequence( process.hltMulti5x5BasicClustersL1NonIsolated + process.hltMulti5x5SuperClustersL1NonIsolated + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTemp + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolated )
process.HLTL1NonIsolatedEcalClustersSequence = cms.Sequence( process.hltHybridSuperClustersL1NonIsolated + process.hltCorrectedHybridSuperClustersL1NonIsolatedTemp + process.hltCorrectedHybridSuperClustersL1NonIsolated + process.HLTMulti5x5SuperClusterL1NonIsolated )
process.HLTEgammaR9ShapeSequence = cms.Sequence( process.hltL1IsoR9shape + process.hltL1NonIsoR9shape )
process.HLTDoLocalHcalWithoutHOSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco )
process.HLTSingleElectronEt10L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt10L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt10EtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt10R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt10HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt10PixelMatchFilter )
process.HLTPixelMatchElectronL1IsoTrackingSequence = cms.Sequence( process.hltCkfL1IsoTrackCandidates + process.hltCtfL1IsoWithMaterialTracks + process.hltPixelMatchElectronsL1Iso )
process.HLTPixelMatchElectronL1NonIsoTrackingSequence = cms.Sequence( process.hltCkfL1NonIsoTrackCandidates + process.hltCtfL1NonIsoWithMaterialTracks + process.hltPixelMatchElectronsL1NonIso )
process.HLTSingleElectronEt12L1NonIsoHLTEleIdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt12EleIdDphiFilter )
process.HLTSingleElectronEt12L1NonIsoHLTTighterEleIdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdDphiFilter )
process.HLTL1IsoEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltL1IsoEgammaRegionalPixelSeedGenerator + process.hltL1IsoEgammaRegionalCkfTrackCandidates + process.hltL1IsoEgammaRegionalCTFFinalFitWithMaterial )
process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence = cms.Sequence( process.hltL1NonIsoEgammaRegionalPixelSeedGenerator + process.hltL1NonIsoEgammaRegionalCkfTrackCandidates + process.hltL1NonIsoEgammaRegionalCTFFinalFitWithMaterial )
process.HLTSingleElectronEt12L1NonIsoHLTTighterEleIdIsolSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolClusterShapeFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TIghterEleIdIsolEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHEFilter + process.hltL1IsolatedPhotonHcalIsol + process.hltL1NonIsolatedPhotonHcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolPixelMatchFilter + process.hltCkfL1IsoTrackCandidates + process.hltCtfL1IsoWithMaterialTracks + process.hltPixelMatchElectronsL1Iso + process.hltCkfL1NonIsoTrackCandidates + process.hltCtfL1NonIsoWithMaterialTracks + process.hltPixelMatchElectronsL1NonIso + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolDphiFilter + process.HLTL1IsoEgammaRegionalRecoTrackerSequence + process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence + process.hltL1IsoElectronTrackIsol + process.hltL1NonIsoElectronTrackIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt12TighterEleIdIsolTrackIsolFilter )
process.HLTSingleElectronEt17L1NonIsoHLTnonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17EtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17PixelMatchFilter )
process.HLTSingleElectronEt17L1NonIsoHLTTightEleIdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdDphiFilter )
process.HLTSingleElectronEt17L1NonIsoHLTTighterEleIdSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdDphiFilter )
process.HLTSingleElectronEt17L1NonIsoHLTTightEleIdIsolSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolClusterShapeFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHEFilter + process.hltL1IsolatedPhotonHcalIsol + process.hltL1NonIsolatedPhotonHcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolPixelMatchFilter + process.hltCkfL1IsoTrackCandidates + process.hltCtfL1IsoWithMaterialTracks + process.hltPixelMatchElectronsL1Iso + process.hltCkfL1NonIsoTrackCandidates + process.hltCtfL1NonIsoWithMaterialTracks + process.hltPixelMatchElectronsL1NonIso + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TIghtEleIdIsolDphiFilter + process.HLTL1IsoEgammaRegionalRecoTrackerSequence + process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence + process.hltL1IsoElectronTrackIsol + process.hltL1NonIsoElectronTrackIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightEleIdIsolTrackIsolFilter )
process.HLTSingleElectronEt17L1NonIsoHLTTighterEleIdIsolSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolClusterShapeFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TIghterEleIdIsolEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHEFilter + process.hltL1IsolatedPhotonHcalIsol + process.hltL1NonIsolatedPhotonHcalIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolPixelMatchFilter + process.hltCkfL1IsoTrackCandidates + process.hltCtfL1IsoWithMaterialTracks + process.hltPixelMatchElectronsL1Iso + process.hltCkfL1NonIsoTrackCandidates + process.hltCtfL1NonIsoWithMaterialTracks + process.hltPixelMatchElectronsL1NonIso + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolDphiFilter + process.HLTL1IsoEgammaRegionalRecoTrackerSequence + process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence + process.hltL1IsoElectronTrackIsol + process.hltL1NonIsoElectronTrackIsol + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TighterEleIdIsolTrackIsolFilter )
process.HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdSC8HE = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HER9ShapeFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEPixelMatchFilter + process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleEtFilter + process.hltActivityR9Shape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleR9ShapeFilter + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdSC8HEDoubleHEFilter )
process.HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdEle8HE = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HER9ShapeFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEPixelMatchFilter + process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleEtFilter + process.hltActivityR9Shape + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleR9ShapeFilter + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoubleHEFilter + process.hltActivityStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt17TightCaloEleIdEle8HEDoublePixelMatchFilter )
process.HLTSingleElectronEt27L1NonIsoHLTTightCaloEleIdTrackSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt27TightCaloEleIdTrackDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt27CaloEleIdTrackDphiFilter )
process.HLTSingleElectronEt32L1NonIsoHLTTightCaloEleIdTrackSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackEtFilter + process.hltL1IsoHLTClusterShape + process.hltL1NonIsoHLTClusterShape + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackClusterShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackHEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackPixelMatchFilter + process.HLTPixelMatchElectronL1IsoTrackingSequence + process.HLTPixelMatchElectronL1NonIsoTrackingSequence + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackOneOEMinusOneOPFilter + process.hltElectronL1IsoDetaDphi + process.hltElectronL1NonIsoDetaDphi + process.hltL1NonIsoHLTNonIsoSingleElectronEt32TightCaloEleIdTrackDetaFilter + process.hltL1NonIsoHLTNonIsoSingleElectronEt32CaloEleIdTrackDphiFilter )
process.HLTDoRegionalEgammaEcalSequenceLowPt = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalEgammaFEDsLowPt + process.hltEcalRegionalEgammaRecHitLowPt + process.hltESRegionalEgammaRecHitLowPt )
process.HLTMulti5x5SuperClusterL1IsolatedLowPt = cms.Sequence( process.hltMulti5x5BasicClustersL1IsolatedLowPt + process.hltMulti5x5SuperClustersL1IsolatedLowPt + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1IsolatedLowPt )
process.HLTL1IsolatedEcalClustersSequenceLowPt = cms.Sequence( process.hltHybridSuperClustersL1IsolatedLowPt + process.hltCorrectedHybridSuperClustersL1IsolatedLowPt + process.HLTMulti5x5SuperClusterL1IsolatedLowPt )
process.HLTMulti5x5SuperClusterL1NonIsolatedLowPt = cms.Sequence( process.hltMulti5x5BasicClustersL1NonIsolatedLowPt + process.hltMulti5x5SuperClustersL1NonIsolatedLowPt + process.hltMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedTempLowPt + process.hltCorrectedMulti5x5EndcapSuperClustersWithPreshowerL1NonIsolatedLowPt )
process.HLTL1NonIsolatedEcalClustersSequenceLowPt = cms.Sequence( process.hltHybridSuperClustersL1NonIsolatedLowPt + process.hltCorrectedHybridSuperClustersL1NonIsolatedTempLowPt + process.hltCorrectedHybridSuperClustersL1NonIsolatedLowPt + process.HLTMulti5x5SuperClusterL1NonIsolatedLowPt )
process.HLTEgammaR9ShapeSequenceLowPt = cms.Sequence( process.hltL1IsoR9shapeLowPt + process.hltL1NonIsoR9shapeLowPt )
process.HLTPixelMatchStartUpWindowElectronL1IsoTrackingSequenceLowPt = cms.Sequence( process.hltCkfL1IsoStartUpWindowTrackCandidatesLowPt + process.hltCtfL1IsoStartUpWindowWithMaterialTracksLowPt + process.hltPixelMatchStartUpWindowElectronsL1IsoLowPt )
process.HLTPixelMatchStartUpWindowElectronL1NonIsoTrackingSequenceLowPt = cms.Sequence( process.hltCkfL1NonIsoStartUpWindowTrackCandidatesLowPt + process.hltCtfL1NonIsoStartUpWindowWithMaterialTracksLowPt + process.hltPixelMatchStartUpWindowElectronsL1NonIsoLowPt )
process.HLTDoublePhotonEt4eeResSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequenceLowPt + process.HLTL1IsolatedEcalClustersSequenceLowPt + process.HLTL1NonIsolatedEcalClustersSequenceLowPt + process.hltL1IsoRecoEcalCandidateLowPt + process.hltL1NonIsoRecoEcalCandidateLowPt + process.hltL1NonIsoDoublePhotonEt4eeResL1MatchFilterRegional + process.hltL1NonIsoDoublePhotonEt4eeResEtFilter + process.HLTEgammaR9ShapeSequenceLowPt + process.hltL1NonIsoHLTNonIsoDoublePhotonEt4eeResR9ShapeFilter + process.hltL1IsoHLTClusterShapeLowPt + process.hltL1NonIsoHLTClusterShapeLowPt + process.hltL1NonIsoDoublePhotonEt4eeResClusterShapeFilter + process.hltL1IsolatedPhotonEcalIsolLowPt + process.hltL1NonIsolatedPhotonEcalIsolLowPt + process.hltL1NonIsoDoublePhotonEt4eeResEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedElectronHcalIsolLowPt + process.hltL1NonIsolatedElectronHcalIsolLowPt + process.hltL1NonIsoDoublePhotonEt4eeResHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeedsLowPt + process.hltL1NonIsoStartUpElectronPixelSeedsLowPt + process.hltL1NonIsoDoublePhotonEt4eeResPixelMatchFilter + process.HLTPixelMatchStartUpWindowElectronL1IsoTrackingSequenceLowPt + process.HLTPixelMatchStartUpWindowElectronL1NonIsoTrackingSequenceLowPt + process.hltL1NonIsoDoublePhotonEt4eeResOneOEMinusOneOPFilter + process.hltL1NonIsoDoublePhotonEt4eeResPMMassFilter )
process.HLTDoubleElectronEt15L1NonIsoHLTnonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoDoubleElectronEt15L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoDoubleElectronEt15EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoDoubleElectronEt15HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoDoubleElectronEt15PixelMatchFilter )
process.HLTSinglePhoton10L1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt10L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt10EtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt10R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt10HEFilter )
process.HLTSinglePhoton15CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedEtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt15CleanedHEFilter )
process.HLTSinglePhotonEt17SC17HEL1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HER9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEHEFilter + process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleEtFilter + process.hltActivityR9Shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleR9ShapeFilter + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt17SC17HEDoubleHEFilter )
process.HLTSinglePhoton20L1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20HEFilter )
process.HLTSinglePhoton20CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt20CleanedHEFilter )
process.HLTSinglePhoton30CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30CleanedHEFilter )
process.HLTSinglePhoton30IsolEBOnlyCleanedL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedR9ShapeFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHEFilter + process.hltL1IsolatedPhotonHcalIsol + process.hltL1NonIsolatedPhotonHcalIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.HLTL1IsoEgammaRegionalRecoTrackerSequence + process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence + process.hltL1IsolatedPhotonHollowTrackIsol + process.hltL1NonIsolatedPhotonHollowTrackIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt30IsolEBOnlyCleanedTrackIsolFilter )
process.HLTSinglePhoton35IsolCleanedL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedR9ShapeFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedEcalIsolFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHEFilter + process.hltL1IsolatedPhotonHcalIsol + process.hltL1NonIsolatedPhotonHcalIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedHcalIsolFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.HLTL1IsoEgammaRegionalRecoTrackerSequence + process.HLTL1NonIsoEgammaRegionalRecoTrackerSequence + process.hltL1IsolatedPhotonHollowTrackIsol + process.hltL1NonIsolatedPhotonHollowTrackIsol + process.hltL1NonIsoHLTNonIsoSinglePhotonEt35IsolCleanedTrackIsolFilter )
process.HLTSinglePhoton50CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedEtFilter + process.HLTEgammaR9ShapeSequence + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50CleanedHEFilter )
process.HLTSinglePhoton50L1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt50HEFilter )
process.HLTSinglePhoton70NoHECleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedEtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt70NoHECleanedHEFilter )
process.HLTSinglePhoton100NoHECleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedEtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt100NoHECleanedHEFilter )
process.HLTDoublePhotonEt5Sequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltDoublePhotonEt5L1MatchFilterRegional + process.hltDoublePhotonEt5EtPhiFilter + process.hltL1IsolatedPhotonEcalIsol + process.hltL1NonIsolatedPhotonEcalIsol + process.hltDoublePhotonEt5EcalIsolFilter + process.HLTDoLocalHcalSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltDoublePhotonEt5HEFilter )
process.HLTDoublePhotonEt17L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoDoublePhotonEt17L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoDoublePhotonEt17EtFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoDoublePhotonEt17HEFilter )
process.HLTCaloTausCreatorRegionalSequence = cms.Sequence( process.HLTDoRegionalJetEcalSequence + process.HLTDoLocalHcalSequence + process.hltTowerMakerForJets + process.hltCaloTowersTau1Regional + process.hltIconeTau1Regional + process.hltCaloTowersTau2Regional + process.hltIconeTau2Regional + process.hltCaloTowersTau3Regional + process.hltIconeTau3Regional + process.hltCaloTowersTau4Regional + process.hltIconeTau4Regional + process.hltCaloTowersCentral1Regional + process.hltIconeCentral1Regional + process.hltCaloTowersCentral2Regional + process.hltIconeCentral2Regional + process.hltCaloTowersCentral3Regional + process.hltIconeCentral3Regional + process.hltCaloTowersCentral4Regional + process.hltIconeCentral4Regional )
process.HLTL2TauJetsSequence = cms.Sequence( process.HLTCaloTausCreatorRegionalSequence + process.hltL2TauJets )
process.HLTL2TauEcalIsolationSequence = cms.Sequence( process.hltL2TauNarrowConeIsolationProducer + process.hltL2TauRelaxingIsolationSelector )
process.HLTMETWithTausSequence = cms.Sequence( process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltTowerMakerForAll + process.hltMet )
process.HLTRecopixelvertexingSequence = cms.Sequence( process.hltPixelTracks + process.hltPixelVertices )
process.HLTL25TauTrackReconstructionSequence = cms.Sequence( process.HLTDoLocalStripSequence + process.hltL25TauPixelSeeds + process.hltL25TauCkfTrackCandidates + process.hltL25TauCtfWithMaterialTracks )
process.HLTL25TauTrackIsolationSequence = cms.Sequence( process.hltL25TauJetTracksAssociator + process.hltL25TauConeIsolation + process.hltL25TauLeadingTrackPtCutSelector )
process.HLTL3TauTrackReconstructionSequence = cms.Sequence( process.hltL3TauPixelSeeds + process.hltL3TauCkfTrackCandidates + process.hltL3TauCtfWithMaterialTracks )
process.HLTL3TauTrackIsolationSequence = cms.Sequence( process.hltL3TauJetTracksAssociator + process.hltL3TauConeIsolation + process.hltL3TauIsolationSelector )
process.HLTL25TauTightTrackIsolationSequence = cms.Sequence( process.hltL25TauJetTracksAssociator + process.hltL25TauConeIsolation + process.hltL25TauLeadingTrackHighPtCutSelector )
process.HLTL3TauHighPtTrackReconstructionSequence = cms.Sequence( process.hltL3TauHighPtPixelSeeds + process.hltL3TauCkfHighPtTrackCandidates + process.hltL3TauCtfWithMaterialHighPtTracks )
process.HLTL3TauHighPtTrackIsolationSequence = cms.Sequence( process.hltL3TauJetHighPtTracksAssociator + process.hltL3TauHighPtConeIsolation + process.hltL3TauHighPtIsolationSelector )
process.HLTBTagMuSequenceL25U = cms.Sequence( process.HLTL2muonrecoNocandSequence + process.hltSelector4JetsU + process.hltBSoftMuonL25JetsU + process.hltBSoftMuonL25TagInfosU + process.hltBSoftMuonL25BJetTagsUByDR )
process.HLTBTagMuSequenceL3U = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonL3TagInfosU + process.hltBSoftMuonL3BJetTagsUByPt + process.hltBSoftMuonL3BJetTagsUByDR )
process.HLTBTagMuSelSequenceL3U = cms.Sequence( process.HLTL3muonrecoNocandSequence + process.hltBSoftMuonL3 + process.hltBSoftMuonSelL3TagInfosU + process.hltBSoftMuonSelL3BJetTagsUByPt + process.hltBSoftMuonSelL3BJetTagsUByDR )
process.HLTSinglePhoton11CleanL1NonIsolatedHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedL1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedEtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedR9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSinglePhotonEt11CleanedHEFilter )
process.HLTSingleMu5Ele5L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSingleMu5Ele5EtFilter + process.hltActivityR9shape + process.hltL1NonIsoHLTNonIsoSingleMu5Ele5R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleMu5Ele5HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltActivityStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleMu5Ele5PixelMatchFilter )
process.HLTSingleMu5Ele9L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTDoRegionalEgammaEcalSequence + process.HLTL1IsolatedEcalClustersSequence + process.HLTL1NonIsolatedEcalClustersSequence + process.hltL1IsoRecoEcalCandidate + process.hltL1NonIsoRecoEcalCandidate + process.hltL1NonIsoHLTNonIsoSingleMu5Ele9L1MatchFilterRegional + process.hltL1NonIsoHLTNonIsoSingleMu5Ele9EtFilter + process.hltL1IsoR9shape + process.hltL1NonIsoR9shape + process.hltL1NonIsoHLTNonIsoSingleMu5Ele9R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltL1IsolatedPhotonHcalForHE + process.hltL1NonIsolatedPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleMu5Ele9HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltL1IsoStartUpElectronPixelSeeds + process.hltL1NonIsoStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleMu5Ele9PixelMatchFilter )
process.HLTSingleEle10MET45L1NonIsoHLTNonIsoSequence = cms.Sequence( process.HLTEcalActivitySequence + process.hltL1NonIsoHLTNonIsoSingleEle10MET45EtFilter + process.hltActivityR9shape + process.hltL1NonIsoHLTNonIsoSingleEle10MET45R9ShapeFilter + process.HLTDoLocalHcalWithoutHOSequence + process.hltActivityPhotonHcalForHE + process.hltL1NonIsoHLTNonIsoSingleEle10MET45HEFilter + process.HLTDoLocalPixelSequence + process.HLTDoLocalStripSequence + process.hltActivityStartUpElectronPixelSeeds + process.hltL1NonIsoHLTNonIsoSingleEle10MET45PixelMatchFilter )
process.HLTPixelTrackingForMinBiasSequence = cms.Sequence( process.hltPixelTracksForMinBias )
process.HLTRecopixelvertexingForMultiVertexSequence = cms.Sequence( process.hltPixelTracks + process.hltPixelVerticesForMultiVertex )
process.HLTL2HcalIsolTrackSequenceHB = cms.Sequence( process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHB + process.hltHITPixelVerticesHB )
process.HLTL2HcalIsolTrackSequenceHE = cms.Sequence( process.HLTDoLocalPixelSequence + process.hltHITPixelTracksHB + process.hltHITPixelTracksHE + process.hltHITPixelVerticesHE )
process.HLTBeginSequenceNZS = cms.Sequence( process.hltTriggerType + process.hltL1EventNumberNZS + process.HLTL1UnpackerSequence + process.hltBPTXCoincidence + process.HLTBeamSpot )
process.HLTRecopixelvertexingForHighMultSequence = cms.Sequence( process.hltPixelTracksForHighMult + process.hltPixelVerticesForHighMult )
process.HLTDoRegionalPi0EtaSequence = cms.Sequence( process.hltESRawToRecHitFacility + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalPi0EtaFEDs + process.hltESRegionalPi0EtaRecHit + process.hltEcalRegionalPi0EtaRecHit )

process.HLT_Activity_CSC = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreActivityCSC + process.hltMuonCSCDigis + process.hltCSCActivityFilter + process.HLTEndSequence )
process.HLT_Activity_DT = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreActivityDT + process.hltMuonDTDigis + process.hltDTTFUnpacker + process.hltDTActivityFilter + process.HLTEndSequence )
process.HLT_Activity_DT_Tuned = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreActivityDTTuned + process.hltMuonDTDigis + process.hltDTTFUnpacker + process.hltDTActivityFilterTuned + process.HLTEndSequence )
process.HLT_Activity_Ecal_SC7 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreActivityEcalSC7 + process.HLTEcalActivitySequence + process.hltEgammaSelectEcalSuperClustersActivityFilterSC7 + process.hltEgammaEcalActivityR9Shape + process.hltEgammaEcalActivityR9ShapeFilterSC7 + process.HLTEndSequence )
process.HLT_Activity_Ecal_SC17 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreActivityEcalSC17 + process.HLTEcalActivitySequence + process.hltEgammaSelectEcalSuperClustersActivityFilterSC17 + process.hltEgammaEcalActivityR9Shape + process.hltEgammaEcalActivityR9ShapeFilterSC17 + process.HLTEndSequence )
process.HLT_L1Jet6U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Jet6U + process.hltPreL1Jet6U_BPTX + process.HLTEndSequence )
process.HLT_L1Jet10U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Jet10U + process.hltPreL1Jet10U_BPTX + process.HLTEndSequence )
process.HLT_Jet15U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet6U + process.hltPreJet15U + process.HLTRecoJetSequenceU + process.hlt1jet15U + process.HLTEndSequence )
process.HLT_Jet15U_HcalNoiseFiltered = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet6U + process.hltPreJet15UHcalNoiseFiltered + process.HLTRecoJetSequenceU + process.hlt1jet15U + process.HLTHcalNoiseSequence + process.HLTEndSequence )
process.HLT_Jet30U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sJet30U + process.hltPreJet30U + process.HLTRecoJetSequenceU + process.hlt1jet30U + process.HLTEndSequence )
process.HLT_Jet50U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sJet50U + process.hltPreJet50U + process.HLTRecoJetSequenceU + process.hlt1jet50U + process.HLTEndSequence )
process.HLT_Jet70U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet40U + process.hltPreJet70U + process.HLTRecoJetSequenceU + process.hlt1jet70U + process.HLTEndSequence )
process.HLT_Jet100U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet60U + process.hltPreJet100U + process.HLTRecoJetSequenceU + process.hlt1jet100U + process.HLTEndSequence )
process.HLT_Jet140U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet60U + process.hltPreJet140U + process.HLTRecoJetSequenceU + process.hlt1jet140U + process.HLTEndSequence )
process.HLT_DiJetAve15U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet6U + process.hltPreDiJetAve15U + process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltDiJetAve15U + process.HLTEndSequence )
process.HLT_DiJetAve30U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet20U + process.hltPreDiJetAve30U + process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltDiJetAve30U + process.HLTEndSequence )
process.HLT_DiJetAve50U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet30U + process.hltPreDiJetAve50U + process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltDiJetAve50U + process.HLTEndSequence )
process.HLT_DiJetAve70U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet40U + process.hltPreDiJetAve70U + process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltDiJetAve70U + process.HLTEndSequence )
process.HLT_DiJetAve100U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet60U + process.hltPreDiJetAve100U + process.HLTDoCaloSequence + process.hltIterativeCone5CaloJets + process.hltDiJetAve100U + process.HLTEndSequence )
process.HLT_DoubleJet15U_ForwardBackward = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet10UEtaOpp + process.hltPreDoubleJet15UForwardBackward + process.HLTRecoJetRegionalSequence + process.hltDoubleJet15UForwardBackward + process.HLTEndSequence )
process.HLT_DoubleJet25U_ForwardBackward = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleForJet10UEtaOpp + process.hltPreDoubleJet25UForwardBackward + process.HLTRecoJetRegionalSequence + process.hltDoubleJet25UForwardBackward + process.HLTEndSequence )
process.HLT_ExclDiJet30U_HFAND_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet20U + process.hltPreExclDiJet30UHFAND + process.HLTRecoJetSequenceU + process.hltExclDiJet30UAND + process.HLTEndSequence )
process.HLT_ExclDiJet30U_HFOR_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet20U + process.hltPreExclDiJet30UHFOR + process.HLTRecoJetSequenceU + process.hltExclDiJet30UOR + process.HLTEndSequence )
process.HLT_QuadJet15U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet8U + process.hltPreQuadJet15U + process.HLTRecoJetSequenceU + process.hlt4jet15U + process.HLTEndSequence )
process.HLT_QuadJet20U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet8U + process.hltPreQuadJet20U + process.HLTRecoJetSequenceU + process.hlt4jet20U + process.HLTEndSequence )
process.HLT_QuadJet25U_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1QuadJet8U + process.hltPreQuadJet25U + process.HLTRecoJetSequenceU + process.hlt4jet25U + process.HLTEndSequence )
process.HLT_L1ETT100 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETT100 + process.hltPreL1ETT100 + process.HLTEndSequence )
process.HLT_L1ETT140_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETT140 + process.hltPreL1ETT140 + process.HLTEndSequence )
process.HLT_EcalOnly_SumEt160_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETT140 + process.hltPreEcalOnlySumEt160 + process.hltEcalRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltTowerMakerForEcalBarrelOnly + process.hltEcalOnlyMet + process.hlt1EcalOnlySumET160 + process.HLTEndSequence )
process.HLT_L1MET20 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1MET20 + process.hltPreL1MET20 + process.HLTEndSequence )
process.HLT_MET45 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET45 + process.HLTRecoMETSequence + process.hlt1MET45 + process.HLTEndSequence )
process.HLT_MET45_HT100U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM20 + process.hltPreMET45HT100U + process.HLTRecoMETSequence + process.hlt1MET45 + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT100U + process.HLTEndSequence )
process.HLT_MET45_HT120U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM20 + process.hltPreMET45HT120U + process.HLTRecoMETSequence + process.hlt1MET45 + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT120U + process.HLTEndSequence )
process.HLT_MET65 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET65 + process.HLTRecoMETSequence + process.hlt1MET65 + process.HLTEndSequence )
process.HLT_MET80_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET80 + process.HLTRecoMETSequence + process.hlt1MET80 + process.HLTEndSequence )
process.HLT_MET100_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETM30 + process.hltPreMET100 + process.HLTRecoMETSequence + process.hlt1MET100 + process.HLTEndSequence )
process.HLT_HT50U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleJet10U + process.hltPreHT50U + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT50U + process.HLTEndSequence )
process.HLT_HT100U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT100U + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT100U + process.HLTEndSequence )
process.HLT_HT120U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT120 + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT120U + process.HLTEndSequence )
process.HLT_HT140U = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT140U + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT140U + process.HLTEndSequence )
process.HLT_HT140U_Eta3_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT140UEta3 + process.HLTRecoJetSequenceU + process.hltJetEta3Ht + process.hltJet20UEta3Ht + process.hltHT140UEta3 + process.HLTEndSequence )
process.HLT_HT160U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT160U + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT160U + process.HLTEndSequence )
process.HLT_HT200U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1HTT50 + process.hltPreHT200U + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT200U + process.HLTEndSequence )
process.HLT_L1MuOpen = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0 + process.hltPreL1MuOpen_BPTX + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1MuOpen_DT = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0 + process.hltPreL1MuOpenDT + process.hltL1MuOpenL1FilteredDT + process.HLTEndSequence )
process.HLT_L1MuOpen_AntiBPTX = cms.Path( process.HLTBeginSequenceAntiBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0 + process.hltPreL1MuOpen_AntiBPTX + process.hltL1MuOpenL1Filtered0 + process.HLTEndSequence )
process.HLT_L1Mu7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreL1Mu7 + process.hltL1Mu7L1Filtered0 + process.HLTEndSequence )
process.HLT_L1Mu20 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu20 + process.hltPreL1Mu20 + process.hltL1Mu20L1Filtered20 + process.HLTEndSequence )
process.HLT_L2Mu0_NoVertex = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu0 + process.hltPreL2Mu0NoVertex + process.hltSingleMu0L1Filtered + process.HLTL2muonrecoSequenceNoVtx + process.hltSingleL2Mu0L2PreFilteredNoVtx + process.HLTEndSequence )
process.HLT_L2Mu7_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreL2Mu7 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTEndSequence )
process.HLT_L2Mu30_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreL2Mu30 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu30L2Filtered30 + process.HLTEndSequence )
process.HLT_Mu3 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu3 + process.hltL1SingleMu0L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu3L2Filtered3 + process.HLTL3muonrecoSequence + process.hltSingleMu3L3Filtered3 + process.HLTEndSequence )
process.HLT_Mu5 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu5 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5L2Filtered4 + process.HLTL3muonrecoSequence + process.hltSingleMu5L3Filtered5 + process.HLTEndSequence )
process.HLT_Mu7 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu5 + process.hltPreMu7 + process.hltL1SingleMu5L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu7L2Filtered5 + process.HLTL3muonrecoSequence + process.hltSingleMu7L3Filtered7 + process.HLTEndSequence )
process.HLT_Mu9 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu9 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL3muonrecoSequence + process.hltSingleMu9L3Filtered9 + process.HLTEndSequence )
process.HLT_Mu11 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu11 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL3muonrecoSequence + process.hltSingleMu11L3Filtered11 + process.HLTEndSequence )
process.HLT_Mu13_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu13 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL3muonrecoSequence + process.hltSingleMu13L3Filtered13 + process.HLTEndSequence )
process.HLT_Mu15_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreMu15 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL3muonrecoSequence + process.hltSingleMu15L3Filtered15 + process.HLTEndSequence )
process.HLT_IsoMu9 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreIsoMu9 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered7 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered9 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered9 + process.HLTEndSequence )
process.HLT_IsoMu11_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu7 + process.hltPreIsoMu11 + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu7L2Filtered7 + process.HLTL2muonisorecoSequence + process.hltSingleMuIsoL2IsoFiltered7 + process.HLTL3muonrecoSequence + process.hltSingleMuIsoL3PreFiltered11 + process.HLTL3muonisorecoSequence + process.hltSingleMuIsoL3IsoFiltered11 + process.HLTEndSequence )
process.HLT_Mu20_NoVertex = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu7 + process.hltPreMu20NoVertex + process.hltL1SingleMu7L1Filtered0 + process.HLTL2muonrecoSequenceNoVtx + process.hltMu20NoVertexL2PreFiltered + process.HLTL3muonrecoSequenceNoVtx + process.hltMu20NoVertexL3PreFiltered20 + process.HLTEndSequence )
process.HLT_L1DoubleMuOpen = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreL1DoubleMuOpen + process.hltDoubleMuLevel1PathL1OpenFiltered + process.HLTEndSequence )
process.HLT_L2DoubleMu0 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreL2DoubleMu0 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTEndSequence )
process.HLT_L2DoubleMu20_NoVertex_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleMuOpen + process.hltPreL2DoubleMu20NoVertex + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequenceNoVtx + process.hltL2DoubleMu20NoVertexL2PreFiltered + process.HLTEndSequence )
process.HLT_DoubleMu0_Quarkonium_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreDoubleMu0Quark + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu0QuarkoniumL3PreFiltered + process.HLTEndSequence )
process.HLT_DoubleMu0_Quarkonium_LS_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreDoubleMu0QuarkLS + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDoubleMu0QuarkoniumLSL3PreFiltered + process.HLTEndSequence )
process.HLT_DoubleMu0 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreDoubleMu0 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDiMuonL3PreFiltered0 + process.HLTEndSequence )
process.HLT_DoubleMu3_v2 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreDoubleMu3 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDiMuonL3PreFiltered3 + process.HLTEndSequence )
process.HLT_DoubleMu5_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreDoubleMu5 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltDiMuonL3PreFiltered5 + process.HLTEndSequence )
process.HLT_Mu5_L2Mu0 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1DoubleMuOpen + process.hltPreMu5L2Mu0 + process.hltDiMuonL1Filtered0 + process.HLTL2muonrecoSequence + process.hltDiMuonL2PreFiltered0 + process.HLTL3muonrecoSequence + process.hltMu5L2Mu0L3Filtered5 + process.HLTEndSequence )
process.HLT_Mu3_Track3_Jpsi = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu3Track3Jpsi + process.hltMu3TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu3TrackJpsiL2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu3TrackJpsiL3Filtered3 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu3TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu3Track3JpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_Mu3_Track5_Jpsi_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu3Track5Jpsi + process.hltMu3TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu3TrackJpsiL2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu3TrackJpsiL3Filtered3 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu3TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu3Track5JpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_Mu5_Track0_Jpsi = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu5Track0Jpsi + process.hltMu5TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu5TrackJpsiL2Filtered4 + process.HLTL3muonrecoSequence + process.hltMu5TrackJpsiL3Filtered5 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu5TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu5TrackJpsiTrackMassFiltered + process.HLTEndSequence )
process.HLT_Mu0_TkMu0_OST_Jpsi = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu0TkMu0Jpsi + process.hltMu0TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu0TrackJpsiL2Filtered0 + process.HLTL3muonrecoSequence + process.hltMu0TrackJpsiL3Filtered0 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu0TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu0TkMuJpsiTrackMassFiltered + process.HLTMuTkMuJpsiTkMuRecoSequence + process.hltMu0TkMuJpsiTkMuMassFiltered + process.HLTEndSequence )
process.HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu0TkMu0JpsiSeagull + process.hltMu0TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu0TrackJpsiL2Filtered0 + process.HLTL3muonrecoSequence + process.hltMu0TrackJpsiL3Filtered0 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu0TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu0TkMuJpsiTrackMassFiltered + process.HLTMuTkMuJpsiTkMuRecoSequence + process.hltMu0TkMuJpsiTkMuMassFilteredTight + process.HLTEndSequence )
process.HLT_Mu3_TkMu0_OST_Jpsi = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMuOpenL1SingleMu0L1SingleMu3 + process.hltPreMu3TkMu0Jpsi + process.hltMu3TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu3TrackJpsiL2Filtered3 + process.HLTL3muonrecoSequence + process.hltMu3TrackJpsiL3Filtered3 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu3TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu3TkMuJpsiTrackMassFiltered + process.HLTMuTkMuJpsiTkMuRecoSequence + process.hltMu3TkMuJpsiTkMuMassFiltered + process.HLTEndSequence )
process.HLT_Mu5_TkMu0_OST_Jpsi = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltPreMu5TkMu0Jpsi + process.hltMu5TrackJpsiL1Filtered0 + process.HLTL2muonrecoSequence + process.hltMu5TrackJpsiL2Filtered4 + process.HLTL3muonrecoSequence + process.hltMu5TrackJpsiL3Filtered5 + process.HLTMuTrackJpsiPixelRecoSequence + process.hltMu5TrackJpsiPixelMassFiltered + process.HLTMuTrackJpsiTrackRecoSequence + process.hltMu5TkMuJpsiTrackMassFiltered + process.HLTMuTkMuJpsiTkMuRecoSequence + process.hltMu5TkMuJpsiTkMuMassFiltered + process.HLTEndSequence )
process.HLT_L1SingleEG2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG2 + process.hltPreL1SingleEG2 + process.HLTEndSequence )
process.HLT_L1SingleEG8 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreL1SingleEG8 + process.HLTEndSequence )
process.HLT_Ele10_SW_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG5 + process.hltPreEle10SWL1R + process.HLTSingleElectronEt10L1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Ele12_SW_TightEleId_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle12SWEleIdL1R + process.HLTSingleElectronEt12L1NonIsoHLTEleIdSequence + process.HLTEndSequence )
process.HLT_Ele12_SW_TighterEleId_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle12SWTighterEleIdL1R + process.HLTSingleElectronEt12L1NonIsoHLTTighterEleIdSequence + process.HLTEndSequence )
process.HLT_Ele12_SW_TighterEleIdIsol_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle12SWTigherEleIdIsolL1R + process.HLTSingleElectronEt12L1NonIsoHLTTighterEleIdIsolSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17SWL1R + process.HLTSingleElectronEt17L1NonIsoHLTnonIsoSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_TightEleId_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17SWTightEleIdL1R + process.HLTSingleElectronEt17L1NonIsoHLTTightEleIdSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_TighterEleId_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17SWTighterEleIdL1R + process.HLTSingleElectronEt17L1NonIsoHLTTighterEleIdSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_TightEleIdIsol_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17SWTightEleIdIsolL1R + process.HLTSingleElectronEt17L1NonIsoHLTTightEleIdIsolSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_TighterEleIdIsol_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17SWTigherEleIdIsolL1R + process.HLTSingleElectronEt17L1NonIsoHLTTighterEleIdIsolSequence + process.HLTEndSequence )
process.HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17TightCaloEleIdSC8HEL1R + process.HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdSC8HE + process.HLTEndSequence )
process.HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle17TightCaloEleIdEle8HEL1R + process.HLTSingleElectronEt17L1NonIsoHLTNonIsoSequenceTightCaloEleIdEle8HE + process.HLTEndSequence )
process.HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle27SWTightCaloEleIdTrackL1R + process.HLTSingleElectronEt27L1NonIsoHLTTightCaloEleIdTrackSequence + process.HLTEndSequence )
process.HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreEle32SWTightCaloEleIdTrackL1R + process.HLTSingleElectronEt32L1NonIsoHLTTightCaloEleIdTrackSequence + process.HLTEndSequence )
process.HLT_DoubleEle4_SW_eeRes_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG2 + process.hltPreDoubleEle4SWeeResL1R + process.HLTDoublePhotonEt4eeResSequence + process.HLTEndSequence )
process.HLT_DoubleEle15_SW_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG5 + process.hltPreDoubleEle15SWL1R + process.HLTDoubleElectronEt15L1NonIsoHLTnonIsoSequence + process.HLTEndSequence )
process.HLT_Photon10_Cleaned_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG5 + process.hltPrePhoton10L1R + process.HLTSinglePhoton10L1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon15_Cleaned_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton15CleanedL1R + process.HLTSinglePhoton15CleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon17_SC17HE_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPreSinglePhoton17SC17HEL1R + process.HLTSinglePhotonEt17SC17HEL1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon20_NoHE_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton20L1R + process.HLTSinglePhoton20L1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon20_Cleaned_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton20CleanedL1R + process.HLTSinglePhoton20CleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon30_Cleaned_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton30CleanedL1R + process.HLTSinglePhoton30CleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePho30IsolEBOnlyL1R + process.HLTSinglePhoton30IsolEBOnlyCleanedL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon35_Isol_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePho35IsolL1R + process.HLTSinglePhoton35IsolCleanedL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon50_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton50HECleanedL1R + process.HLTSinglePhoton50CleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon50_NoHE_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton50L1R + process.HLTSinglePhoton50L1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon70_NoHE_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton70NoHECleanedL1R + process.HLTSinglePhoton70NoHECleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Photon100_NoHE_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleEG8 + process.hltPrePhoton100NoHECleanedL1R + process.HLTSinglePhoton100NoHECleanL1NonIsolatedHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_DoublePhoton5_CEP_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG5 + process.hltPreDoublePhoton5CEPL1R + process.HLTDoublePhotonEt5Sequence + process.hltTowerMakerForHcal + process.hltHcalTowerFilter + process.HLTEndSequence )
process.HLT_DoublePhoton17_L1R = cms.Path( process.HLTBeginSequence + process.hltL1sL1DoubleEG5 + process.hltPreDoublePhoton17L1R + process.HLTDoublePhotonEt17L1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_SingleIsoTau20_Trk5_MET20 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleIsoTau20Trk5MET20 + process.hltPreSingleIsoTau20Trk5MET20 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutSingleIsoTau20Trk5MET20 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationSingleIsoTau20Trk5MET20 + process.HLTMETWithTausSequence + process.hltFilterL2TauMET20 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTrackIsolationSequence + process.hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk5MET20 + process.HLTL3TauTrackReconstructionSequence + process.HLTL3TauTrackIsolationSequence + process.hltL1HLTSingleIsoTau20Trk5MET20JetsMatch + process.hltFilterL3TrackIsolationSingleIsoTau20Trk5MET20 + process.HLTEndSequence )
process.HLT_SingleIsoTau20_Trk15_MET20 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleIsoTau20Trk15MET20 + process.hltPreSingleIsoTau20Trk15MET20 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutSingleIsoTau20Trk15MET20 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationSingleIsoTau20Trk15MET20 + process.HLTMETWithTausSequence + process.hltFilterL2TauMET20 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTightTrackIsolationSequence + process.hltFilterL25LeadingTrackPtCutSingleIsoTau20Trk15MET20 + process.HLTL3TauHighPtTrackReconstructionSequence + process.HLTL3TauHighPtTrackIsolationSequence + process.hltL1HLTSingleIsoTau20Trk15MET20JetsMatch + process.hltFilterL3TrackIsolationSingleIsoTau20Trk15MET20 + process.HLTEndSequence )
process.HLT_SingleIsoTau30_Trk5_MET20 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sSingleIsoTau30Trk5MET20 + process.hltPreSingleIsoTau30Trk5MET20 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutSingleIsoTau30Trk5MET20 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationSingleIsoTau30Trk5MET20 + process.HLTMETWithTausSequence + process.hltFilterL2TauMET20 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTrackIsolationSequence + process.hltFilterL25LeadingTrackPtCutSingleIsoTau30Trk5MET20 + process.HLTL3TauTrackReconstructionSequence + process.HLTL3TauTrackIsolationSequence + process.hltL1HLTSingleIsoTau30Trk5MET20JetsMatch + process.hltFilterL3TrackIsolationSingleIsoTau30Trk5MET20 + process.HLTEndSequence )
process.HLT_SingleIsoTau30_Trk5_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sSingleIsoTau30L120or30Trk5 + process.hltPreSingleIsoTau30L120or30Trk5 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutSingleIsoTau30L120or30Trk5 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationSingleIsoTau30L120or30Trk5 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTrackIsolationSequence + process.hltFilterL25LeadingTrackPtCutSingleIsoTau30L120or30Trk5 + process.HLTL3TauTrackReconstructionSequence + process.HLTL3TauTrackIsolationSequence + process.hltL1HLTSingleIsoTau30L120or30Trk5JetsMatch + process.hltFilterL3TrackIsolationSingleIsoTau30L120or30Trk5 + process.HLTEndSequence )
process.HLT_DoubleIsoTau15_OneLeg_Trk5 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sDoubleOneLegIsoTau15Trk5 + process.hltPreDoubleOneLegIsoTau15Trk5 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutDoubleOneLegIsoTau15Trk5 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationDoubleOneLegIsoTau15Trk5 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTrackIsolationSequence + process.hltL1L25DoubleOneLegIsoTau15Trk5JetsMatch + process.hltFilterL25LeadingTrackPtCutDoubleOneLegIsoTau15Trk5 + process.HLTL3TauTrackReconstructionSequence + process.HLTL3TauTrackIsolationSequence + process.hltL1HLTDoubleOneLegIsoTau15Trk5JetsMatch + process.hltFilterL3TrackIsolationDoubleOneLegIsoTau15Trk5 + process.HLTEndSequence )
process.HLT_DoubleIsoTau15_Trk5 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sDoubleIsoTau15Trk5 + process.hltPreDoubleIsoTau15Trk5 + process.HLTL2TauJetsSequence + process.hltFilterL2EtCutDoubleIsoTau15Trk5 + process.HLTL2TauEcalIsolationSequence + process.hltFilterL2EcalIsolationDoubleIsoTau15Trk5 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingSequence + process.HLTL25TauTrackReconstructionSequence + process.HLTL25TauTrackIsolationSequence + process.hltFilterL25LeadingTrackPtCutDoubleIsoTau15Trk5 + process.HLTL3TauTrackReconstructionSequence + process.HLTL3TauTrackIsolationSequence + process.hltL1HLTDoubleIsoTau15Trk5JetsMatch + process.hltFilterL3TrackIsolationDoubleIsoTau15Trk5 + process.HLTEndSequence )
process.HLT_BTagMu_DiJet10U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sBTagMuDiJet10U + process.hltPreBTagMuDiJet10U + process.HLTRecoJetSequenceU + process.hltBDiJet10U + process.HLTBTagMuSequenceL25U + process.hltBSoftMuonL25FilterUByDR + process.HLTBTagMuSequenceL3U + process.hltBSoftMuonL3FilterUByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet20U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sBTagMuDiJet10U + process.hltPreBTagMuDiJet20U + process.HLTRecoJetSequenceU + process.hltBDiJet20U + process.HLTBTagMuSequenceL25U + process.hltBSoftMuonL25FilterUByDR + process.HLTBTagMuSequenceL3U + process.hltBSoftMuonL3FilterUByDR + process.HLTEndSequence )
process.HLT_BTagMu_DiJet20U_Mu5_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sBTagMuDiJet10U + process.hltPreBTagMuDiJet20UMu5 + process.HLTRecoJetSequenceU + process.hltBDiJet20U + process.HLTBTagMuSequenceL25U + process.hltBSoftMuonL25FilterUByDR + process.HLTBTagMuSelSequenceL3U + process.hltBSoftMuonSelL3FilterUByDR + process.HLTEndSequence )
process.HLT_StoppedHSCP20_v3 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet10UNotBptxOR + process.hltPreStoppedHSCP20 + process.hltHcalDigis + process.hltHbhereco + process.hltStoppedHSCPHpdFilter + process.hltStoppedHSCPTowerMakerForAll + process.hltStoppedHSCPIterativeCone5CaloJets + process.hltStoppedHSCP1CaloJetEnergy20 + process.HLTEndSequence )
process.HLT_StoppedHSCP35_v3 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleJet10UNotBptxOR + process.hltPreStoppedHSCP35 + process.hltHcalDigis + process.hltHbhereco + process.hltStoppedHSCPHpdFilter + process.hltStoppedHSCPTowerMakerForAll + process.hltStoppedHSCPIterativeCone5CaloJets + process.hltStoppedHSCP1CaloJetEnergy35 + process.HLTEndSequence )
process.HLT_Mu5_Photon11_Cleaned_L1R_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3EG5 + process.hltPreMu5Photon11CleanedL1R + process.HLTSinglePhoton11CleanL1NonIsolatedHLTNonIsoSequence + process.hltL1SingleMu3EG5L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5EG5L2Filtered4 + process.HLTL3muonrecoSequence + process.hltSingleMu5EG5L3Filtered5 + process.HLTEndSequence )
process.HLT_Mu5_Ele5_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1SingleMu3 + process.hltPreMu5Ele5 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5L2Filtered4 + process.HLTL3muonrecoSequence + process.hltSingleMu5L3Filtered5 + process.HLTSingleMu5Ele5L1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Mu5_Ele9_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3EG5 + process.hltPreMu5Ele9 + process.hltL1SingleMu3EG5L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5EG5L2Filtered4 + process.HLTL3muonrecoSequence + process.hltSingleMu5EG5L3Filtered5 + process.HLTSingleMu5Ele9L1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_Mu5_Jet35U_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3Jet10U + process.hltPreMu5Jet35U + process.hltL1Mu3Jet10UL1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu5Jet10UL2Filtered4 + process.HLTL3muonrecoSequence + process.hltL3Mu5Jet10UL3Filtered5 + process.HLTRecoJetSequenceU + process.hlt1jet35U + process.HLTEndSequence )
process.HLT_Mu5_Jet50U_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sL1Mu3Jet10U + process.hltPreMu5Jet50U + process.hltL1Mu3Jet10UL1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu5Jet10UL2Filtered4 + process.HLTL3muonrecoSequence + process.hltL3Mu5Jet10UL3Filtered5 + process.HLTRecoJetSequenceU + process.hlt1jet50U + process.HLTEndSequence )
process.HLT_Mu5_MET45_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1SingleMu3 + process.hltL1sL1ETM20 + process.hltPreMu5MET45 + process.hltL1SingleMu3L1Filtered0 + process.HLTL2muonrecoSequence + process.hltSingleMu5L2Filtered4 + process.HLTL3muonrecoSequence + process.hltSingleMu5L3Filtered5 + process.HLTRecoMETSequence + process.hlt1MET45 + process.HLTEndSequence )
process.HLT_Mu5_HT50U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3Jet10U + process.hltPreMu5HT50U + process.hltL1Mu3Jet10UL1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu5Jet10UL2Filtered4 + process.HLTL3muonrecoSequence + process.hltL3Mu5Jet10UL3Filtered5 + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT50U + process.HLTEndSequence )
process.HLT_Mu5_HT70U_v1 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1Mu3Jet10U + process.hltPreMu5HT70U + process.hltL1Mu3Jet10UL1Filtered0 + process.HLTL2muonrecoSequence + process.hltL2Mu5Jet10UL2Filtered4 + process.HLTL3muonrecoSequence + process.hltL3Mu5Jet10UL3Filtered5 + process.HLTRecoJetSequenceU + process.HLTDoJet20UHTRecoSequence + process.hltHT70 + process.HLTEndSequence )
process.HLT_Ele10_MET45_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ETM20 + process.hltPreEle10MET45 + process.HLTRecoMETSequence + process.hlt1MET45 + process.HLTSingleEle10MET45L1NonIsoHLTNonIsoSequence + process.HLTEndSequence )
process.HLT_ZeroBias = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreZeroBias + process.HLTEndSequence )
process.HLT_ZeroBiasPixel_SingleTrack = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreZeroBiasPixelSingleTrack + process.HLTDoLocalPixelSequence + process.HLTPixelTrackingForMinBiasSequence + process.hltPixelCandsForMinBias + process.hltMinBiasPixelFilter1 + process.HLTEndSequence )
process.HLT_MinBiasPixel_SingleTrack = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreMinBiasPixelSingleTrack + process.hltL1TechBSCminBiasOR + process.HLTDoLocalPixelSequence + process.HLTPixelTrackingForMinBiasSequence + process.hltPixelCandsForMinBias + process.hltMinBiasPixelFilter1 + process.HLTEndSequence )
process.HLT_MultiVertex6 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreMultiVertex6 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForMultiVertexSequence + process.hltVertexFilter6 + process.HLTEndSequence )
process.HLT_MultiVertex8_L1ETT60 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT60 + process.hltPreMultiVertex8 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForMultiVertexSequence + process.hltVertexFilter8 + process.HLTEndSequence )
process.HLT_L1_BptxXOR_BscMinBiasOR = cms.Path( process.HLTBeginSequence + process.hltL1sL1BptxXORBscMinBiasOR + process.hltPreL1BptxXORBscMinBiasOR + process.HLTEndSequence )
process.HLT_L1Tech_BSC_minBias_OR = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreL1TechBSCminBiasOR + process.hltL1TechBSCminBiasOR + process.HLTEndSequence )
process.HLT_L1Tech_BSC_minBias = cms.Path( process.HLTBeginSequence + process.hltL1sZeroBias + process.hltPreL1TechBSCminBias + process.hltL1TechBSCminBias + process.HLTEndSequence )
process.HLT_L1Tech_BSC_halo = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreL1TechBSChalo + process.hltL1TechBSChalo + process.HLTEndSequence )
process.HLT_L1Tech_BSC_halo_forPhysicsBackground = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreL1TechBSChalo_forPhysicsBackground + process.hltL1TechBSChalo + process.HLTEndSequence )
process.HLT_L1Tech_BSC_HighMultiplicity = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sHighMultiplicityBSC + process.hltPreHighMultiplicityBSC + process.HLTEndSequence )
process.HLT_L1Tech_RPC_TTU_RBst1_collisions = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1TechRPCTTURBst1collisions + process.hltPreL1TechRPCTTURBst1collisions + process.HLTEndSequence )
process.HLT_L1Tech_HCAL_HF = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sZeroBias + process.hltPreL1HFTech + process.hltL1TechHCALHF + process.HLTEndSequence )
process.HLT_TrackerCosmics = cms.Path( process.HLTBeginSequence + process.hltL1sTrackerCosmics + process.hltPreTrackerCosmics + process.hltTrackerCosmicsPattern + process.HLTEndSequence )
process.HLT_IsoTrackHB_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sIsoTrackHB8E29 + process.hltPreIsoTrackHB8E29 + process.HLTL2HcalIsolTrackSequenceHB + process.hltIsolPixelTrackProdHB8E29 + process.hltIsolPixelTrackL2FilterHB8E29 + process.HLTDoLocalStripSequence + process.hltHITPixelTripletSeedGeneratorHB8E29 + process.hltHITCkfTrackCandidatesHB8E29 + process.hltHITCtfWithMaterialTracksHB8E29 + process.hltHITIPTCorrectorHB8E29 + process.hltIsolPixelTrackL3FilterHB8E29 + process.HLTEndSequence )
process.HLT_IsoTrackHE_v2 = cms.Path( process.HLTBeginSequence + process.hltL1sIsoTrackHE8E29 + process.hltPreIsoTrackHE8E29 + process.HLTL2HcalIsolTrackSequenceHE + process.hltIsolPixelTrackProdHE8E29 + process.hltIsolPixelTrackL2FilterHE8E29 + process.HLTDoLocalStripSequence + process.hltHITPixelTripletSeedGeneratorHE8E29 + process.hltHITCkfTrackCandidatesHE8E29 + process.hltHITCtfWithMaterialTracksHE8E29 + process.hltHITIPTCorrectorHE8E29 + process.hltIsolPixelTrackL3FilterHE8E29 + process.HLTEndSequence )
process.HLT_RPCBarrelCosmics = cms.Path( process.HLTBeginSequence + process.hltL1sRPCBarrelCosmics + process.hltPreRPCBarrelCosmics + process.HLTEndSequence )
process.HLT_HcalPhiSym = cms.Path( process.HLTBeginSequenceNZS + process.hltLevel1Activity + process.hltPreHcalPhiSym + process.HLTEndSequence )
process.HLT_HcalNZS = cms.Path( process.HLTBeginSequenceNZS + process.hltL1sHcalNZS8E29 + process.hltPreHcalNZS8E29 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity70 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT60 + process.hltPrePixelTracksMultiplicity70 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultSequence + process.hltPixelCandsForHighMult + process.hlt1HighMult70 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity85 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sETT60 + process.hltPrePixelTracksMultiplicity85 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultSequence + process.hltPixelCandsForHighMult + process.hlt1HighMult85 + process.HLTEndSequence )
process.HLT_PixelTracks_Multiplicity100 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1ETT100 + process.hltPrePixelTracksMultiplicity100 + process.HLTDoLocalPixelSequence + process.HLTRecopixelvertexingForHighMultSequence + process.hltPixelCandsForHighMult + process.hlt1HighMult100 + process.HLTEndSequence )
process.HLT_GlobalRunHPDNoise = cms.Path( process.HLTBeginSequence + process.hltL1sGlobalRunHPDNoise + process.hltPreGlobalRunHPDNoise + process.HLTEndSequence )
process.HLT_TechTrigHCALNoise = cms.Path( process.HLTBeginSequence + process.hltL1sTechTrigHCALNoise + process.hltL1sNotBptxPlusOrMinus + process.hltPreTechTrigHCALNoise + process.HLTEndSequence )
process.HLT_L1_BPTX = cms.Path( process.HLTBeginSequence + process.hltL1sL1BPTX + process.hltPreL1BPTX + process.HLTEndSequence )
process.HLT_L1_BPTX_MinusOnly = cms.Path( process.HLTBeginSequence + process.hltL1sL1BPTXMinusOnly + process.hltPreL1BPTXMinusOnly + process.HLTEndSequence )
process.HLT_L1_BPTX_PlusOnly = cms.Path( process.HLTBeginSequence + process.hltL1sL1BPTXPlusOnly + process.hltPreL1BPTXPlusOnly + process.HLTEndSequence )
process.HLT_DTErrors = cms.Path( process.hltGtDigis + process.hltPreAlCaDTErrors + process.hltDTROMonitorFilter + process.hltDynAlCaDTErrors + process.HLTEndSequence )
process.HLT_LogMonitor = cms.Path( process.hltGtDigis + process.hltPreLogMonitor + process.hltLogMonitorFilter + process.HLTEndSequence )
process.HLT_Calibration = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreCalibration + process.HLTEndSequence )
process.HLT_EcalCalibration = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreEcalCalibration + process.hltEcalCalibrationRaw + process.HLTEndSequence )
process.HLT_HcalCalibration = cms.Path( process.hltCalibrationEventsFilter + process.hltGtDigis + process.hltPreHcalCalibration + process.hltHcalCalibTypeFilter + process.HLTEndSequence )
process.HLT_Random = cms.Path( process.hltRandomEventsFilter + process.HLTL1UnpackerSequence + process.hltPreRandom + process.HLTEndSequence )
process.AlCa_EcalPhiSym = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sL1BscMinBiasORBptxPlusANDMinus + process.hltPreAlCaEcalPhiSym + process.hltEcalRawToRecHitFacility + process.hltESRawToRecHitFacility + process.hltEcalRegionalRestFEDs + process.hltEcalRecHitAll + process.hltAlCaPhiSymStream + process.HLTEndSequence )
process.AlCa_EcalPi0 = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta8E29 + process.hltPreAlCaEcalPi08E29 + process.HLTDoRegionalPi0EtaSequence + process.hltSimple3x3Clusters + process.hltAlCaPi0RecHitsFilter + process.HLTEndSequence )
process.AlCa_EcalEta = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaEcalPi0Eta8E29 + process.hltPreAlCaEcalEta8E29 + process.HLTDoRegionalPi0EtaSequence + process.hltSimple3x3Clusters + process.hltAlCaEtaRecHitsFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNoHits = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoHits + process.HLTmuonlocalrecoSequence + process.hltRPCPointProducer + process.hltRPCFilter + process.HLTEndSequence )
process.AlCa_RPCMuonNoTriggers = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNoTriggers + process.hltRPCMuonNoTriggersL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.AlCa_RPCMuonNormalisation = cms.Path( process.HLTBeginSequenceBPTX + process.hltL1sAlCaRPC + process.hltPreRPCMuonNorma + process.hltRPCMuonNormaL1Filtered0 + process.HLTmuonlocalrecoSequence + process.HLTEndSequence )
process.DQM_FEDIntegrity = cms.Path( process.HLTBeginSequence + process.hltPreFEDIntegrity + process.hltDTDQMEvF + process.hltEcalDigis + process.hltEBHltTask + process.hltEEHltTask + process.hltL1tfed + process.hltSiPixelDigisWithErrors + process.hltSiPixelHLTSource + process.hltSiStripFEDCheck + process.hltMuonRPCDigis + process.hltRPCFEDIntegrity + process.hltBoolFalse )
process.HLTriggerFinalPath = cms.Path( process.hltGtDigis + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW + process.hltBoolTrue )

process.HLTOutput = cms.EndPath( process.hltOutputA )
process.ExpressOutput = cms.EndPath( process.hltPreExpress + process.hltPreExpressSmart + process.hltOutputExpress )
process.AlCaOutput = cms.EndPath( process.hltOutputALCAP0 )
process.DQMOutput = cms.EndPath( process.hltDQML1Scalers + process.hltDQML1SeedLogicScalers + process.hltDQMHLTScalers + process.hltPreDQM + process.hltPreDQMSmart + process.hltOutputDQM )
process.HLTDQMOutput = cms.EndPath( process.hltPreHLTDQM + process.hltPreHLTDQMSmart + process.hltOutputHLTDQM )
process.HLTDQMResultsOutput = cms.EndPath( process.hltPreHLTDQMResults + process.hltPreHLTDQMResultsSmart + process.hltOutputHLTDQMResults )
process.HLTMONOutput = cms.EndPath( process.hltPreHLTMON + process.hltPreHLTMONSmart + process.hltOutputHLTMON )
process.NanoDSTOutput = cms.EndPath( process.hltPreNanoDST + process.hltOutputNanoDST )

process.HLTSchedule = cms.Schedule( process.HLT_Activity_CSC, process.HLT_Activity_DT, process.HLT_Activity_DT_Tuned, process.HLT_Activity_Ecal_SC7, process.HLT_Activity_Ecal_SC17, process.HLT_L1Jet6U, process.HLT_L1Jet10U, process.HLT_Jet15U, process.HLT_Jet15U_HcalNoiseFiltered, process.HLT_Jet30U, process.HLT_Jet50U, process.HLT_Jet70U_v2, process.HLT_Jet100U_v2, process.HLT_Jet140U_v1, process.HLT_DiJetAve15U, process.HLT_DiJetAve30U, process.HLT_DiJetAve50U, process.HLT_DiJetAve70U_v2, process.HLT_DiJetAve100U_v1, process.HLT_DoubleJet15U_ForwardBackward, process.HLT_DoubleJet25U_ForwardBackward, process.HLT_ExclDiJet30U_HFAND_v1, process.HLT_ExclDiJet30U_HFOR_v1, process.HLT_QuadJet15U_v2, process.HLT_QuadJet20U_v2, process.HLT_QuadJet25U_v2, process.HLT_L1ETT100, process.HLT_L1ETT140_v1, process.HLT_EcalOnly_SumEt160_v2, process.HLT_L1MET20, process.HLT_MET45, process.HLT_MET45_HT100U_v1, process.HLT_MET45_HT120U_v1, process.HLT_MET65, process.HLT_MET80_v1, process.HLT_MET100_v2, process.HLT_HT50U_v1, process.HLT_HT100U, process.HLT_HT120U, process.HLT_HT140U, process.HLT_HT140U_Eta3_v1, process.HLT_HT160U_v1, process.HLT_HT200U_v1, process.HLT_L1MuOpen, process.HLT_L1MuOpen_DT, process.HLT_L1MuOpen_AntiBPTX, process.HLT_L1Mu7_v1, process.HLT_L1Mu20, process.HLT_L2Mu0_NoVertex, process.HLT_L2Mu7_v1, process.HLT_L2Mu30_v1, process.HLT_Mu3, process.HLT_Mu5, process.HLT_Mu7, process.HLT_Mu9, process.HLT_Mu11, process.HLT_Mu13_v1, process.HLT_Mu15_v1, process.HLT_IsoMu9, process.HLT_IsoMu11_v1, process.HLT_Mu20_NoVertex, process.HLT_L1DoubleMuOpen, process.HLT_L2DoubleMu0, process.HLT_L2DoubleMu20_NoVertex_v1, process.HLT_DoubleMu0_Quarkonium_v1, process.HLT_DoubleMu0_Quarkonium_LS_v1, process.HLT_DoubleMu0, process.HLT_DoubleMu3_v2, process.HLT_DoubleMu5_v1, process.HLT_Mu5_L2Mu0, process.HLT_Mu3_Track3_Jpsi, process.HLT_Mu3_Track5_Jpsi_v1, process.HLT_Mu5_Track0_Jpsi, process.HLT_Mu0_TkMu0_OST_Jpsi, process.HLT_Mu0_TkMu0_OST_Jpsi_Tight_v1, process.HLT_Mu3_TkMu0_OST_Jpsi, process.HLT_Mu5_TkMu0_OST_Jpsi, process.HLT_L1SingleEG2, process.HLT_L1SingleEG8, process.HLT_Ele10_SW_L1R, process.HLT_Ele12_SW_TightEleId_L1R, process.HLT_Ele12_SW_TighterEleId_L1R_v1, process.HLT_Ele12_SW_TighterEleIdIsol_L1R_v1, process.HLT_Ele17_SW_L1R, process.HLT_Ele17_SW_TightEleId_L1R, process.HLT_Ele17_SW_TighterEleId_L1R_v1, process.HLT_Ele17_SW_TightEleIdIsol_L1R_v1, process.HLT_Ele17_SW_TighterEleIdIsol_L1R_v1, process.HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R_v1, process.HLT_Ele17_SW_TightCaloEleId_Ele8HE_L1R_v1, process.HLT_Ele27_SW_TightCaloEleIdTrack_L1R_v1, process.HLT_Ele32_SW_TightCaloEleIdTrack_L1R_v1, process.HLT_DoubleEle4_SW_eeRes_L1R, process.HLT_DoubleEle15_SW_L1R_v1, process.HLT_Photon10_Cleaned_L1R, process.HLT_Photon15_Cleaned_L1R, process.HLT_Photon17_SC17HE_L1R_v1, process.HLT_Photon20_NoHE_L1R, process.HLT_Photon20_Cleaned_L1R, process.HLT_Photon30_Cleaned_L1R, process.HLT_Photon30_Isol_EBOnly_Cleaned_L1R_v1, process.HLT_Photon35_Isol_Cleaned_L1R_v1, process.HLT_Photon50_Cleaned_L1R_v1, process.HLT_Photon50_NoHE_L1R, process.HLT_Photon70_NoHE_Cleaned_L1R_v1, process.HLT_Photon100_NoHE_Cleaned_L1R_v1, process.HLT_DoublePhoton5_CEP_L1R, process.HLT_DoublePhoton17_L1R, process.HLT_SingleIsoTau20_Trk5_MET20, process.HLT_SingleIsoTau20_Trk15_MET20, process.HLT_SingleIsoTau30_Trk5_MET20, process.HLT_SingleIsoTau30_Trk5_v2, process.HLT_DoubleIsoTau15_OneLeg_Trk5, process.HLT_DoubleIsoTau15_Trk5, process.HLT_BTagMu_DiJet10U_v1, process.HLT_BTagMu_DiJet20U_v1, process.HLT_BTagMu_DiJet20U_Mu5_v1, process.HLT_StoppedHSCP20_v3, process.HLT_StoppedHSCP35_v3, process.HLT_Mu5_Photon11_Cleaned_L1R_v1, process.HLT_Mu5_Ele5_v1, process.HLT_Mu5_Ele9_v1, process.HLT_Mu5_Jet35U_v1, process.HLT_Mu5_Jet50U_v2, process.HLT_Mu5_MET45_v1, process.HLT_Mu5_HT50U_v1, process.HLT_Mu5_HT70U_v1, process.HLT_Ele10_MET45_v1, process.HLT_ZeroBias, process.HLT_ZeroBiasPixel_SingleTrack, process.HLT_MinBiasPixel_SingleTrack, process.HLT_MultiVertex6, process.HLT_MultiVertex8_L1ETT60, process.HLT_L1_BptxXOR_BscMinBiasOR, process.HLT_L1Tech_BSC_minBias_OR, process.HLT_L1Tech_BSC_minBias, process.HLT_L1Tech_BSC_halo, process.HLT_L1Tech_BSC_halo_forPhysicsBackground, process.HLT_L1Tech_BSC_HighMultiplicity, process.HLT_L1Tech_RPC_TTU_RBst1_collisions, process.HLT_L1Tech_HCAL_HF, process.HLT_TrackerCosmics, process.HLT_IsoTrackHB_v2, process.HLT_IsoTrackHE_v2, process.HLT_RPCBarrelCosmics, process.HLT_HcalPhiSym, process.HLT_HcalNZS, process.HLT_PixelTracks_Multiplicity70, process.HLT_PixelTracks_Multiplicity85, process.HLT_PixelTracks_Multiplicity100, process.HLT_GlobalRunHPDNoise, process.HLT_TechTrigHCALNoise, process.HLT_L1_BPTX, process.HLT_L1_BPTX_MinusOnly, process.HLT_L1_BPTX_PlusOnly, process.HLT_DTErrors, process.HLT_LogMonitor, process.HLT_Calibration, process.HLT_EcalCalibration, process.HLT_HcalCalibration, process.HLT_Random, process.AlCa_EcalPhiSym, process.AlCa_EcalPi0, process.AlCa_EcalEta, process.AlCa_RPCMuonNoHits, process.AlCa_RPCMuonNoTriggers, process.AlCa_RPCMuonNormalisation, process.DQM_FEDIntegrity, process.HLTriggerFinalPath, process.HLTOutput, process.ExpressOutput, process.AlCaOutput, process.DQMOutput, process.HLTDQMOutput, process.HLTDQMResultsOutput, process.HLTMONOutput, process.NanoDSTOutput )
