"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
"""

amostra = """
vvMQnwwvrwWNfrtZJfppmSfJSmSg
BzGqjlBqBBmztHNFzDHg
llRCPlTPPqBjPhqhlBRBClhqWcTWrWNcMbQbdrdLccccrnvM
wMhwbTWpQjbpWHMQppzTHhjtlCjPSSJCCtlqRlJVFJFt
ggdvvnvDgdDmNcBrrcDntFRFqHJJtSJqvlVSRlJq
fggNNffGmcBrmBfcDzzzpHbsGTpszwwTbp
BPdPPBggrPtrpbtvPBBdgrFmhhQThGGlbbTZnzZQzZfn
ccjWRJVNcTGmnWWFmh
DMNmsMHwRNBrggdPDPdt
TfsfHLQbBtBFQbQsBmPwwlnPGZFwwdwWFZZw
MRpcvJMJVSMrVMpVSvhhnclwgWwDZgWgWgWglwcG
GCzjRJjVjSSrvfNQtLmQNsQbjB
FrSPFjtVvwsqSwcG
hDHdWDngpgZTDgHzzHwNNqlwNvZJlGqcQGsl
wDzLTDHgFffLtRft
CnCJNVqvCBJBNZmfPcPMcFLVcwmd
HgzjHFghSFtrLfwPchPM
QDpjgDSQlHHlDQQRzRzsBRRvWnWvJvZnqWBJNF
mGHcFPFqzPtcfPwDGVVpgLgSlgBl
rCvddTrnsbDLVSDwjSjd
QWhWQThswssMQMMMvhTzPqJzmzftHccJfHFhFm
cPbNpLVFTPbbFrpTLQBzqqmgnnBhgLMM
vvSwWCZCRZCDZtGwzdgWdQmzqgnQddJn
vCltGltCGmRRmCvDjjtHFpbcFfbbfssbpNPpHFpH
WLLQMWZLSPMPWmrwhnjhZZhpHJHljBDB
csbtCfFgCftGljHwHcBnpnJR
tsvgszNtfMwPzWqPrS
NbDZrbrFQQqqQtQqQDtTcBvCLBLswsZhscCGBZ
ljmWRzVRpbndMWmmfdsTsCBsGwTVVVCGCGws
ffRpnllHRMfdWzdnmRNQNNSFQQFNbrFHHrNH
LccGzWNjcvNLGTmHNsNLMlMwMpMPGlMCwFwDDGCw
fZZtfrZgrfQSnnnSnJRCglHpCwwHwpglDClFMw
SqJQnffJRnfQQVRhrQtrhnThcLhzNzHdTjhsTWzjdmcm
QJQwJMSbtbRgMQMQVZpCZsrrhpZBwrLLvs
qCNPGWdqhpphsWrB
DcNPNnqjdGDqjmPGGJRFMQmgtlQmQJCSgb
blTRbDnHRGGBwnGPCtFPWzVCDvFWtL
pdSJprqhhZSdqSdZNhVzZWtzLVgVPvzjLzWv
rrsqsmrMpPHlwTsRHn
mbNhgbRSLmTwswFm
vHjHBWMHBzMqWZVZBzHzcwwwdcFLcpLspdzwpwQd
HfMWMfvjWtZHqWDlhSnnnJNnbhslDb
lwsvPPnqlwwwsPcHTgqcRcSccmgQ
CVWBWCFpFzWfFjWjhNSQJJmcVcHRZJNTSc
zdhfzBtfLLtfFClbrDvsPvtPbnmv
PntVQbDnQHcDVvhtbtDhcbPcFTrrNfjqmmPTTZqMLZZMjFZm
lgJCpCFCSCGCpllWMfZqTNNZrMjrJTTM
CSzSwgFlzsGBzQcQhsnnDbVdtc
THzqvrVrWzhqhWwqhTbNNDRtFRmmpFDDVsFLLsdddF
MbZSSScZSGCJCjZlCjdPmpRmFLDtctdmFRsp
GfJQlnZjSMnllbJCQbClnZQrhNwwqhBzTNhrffqhqWhTqz
BdBdmDZHFFbrHHStPSRtPCzSRNDS
JGGpwqLJGMTLpLlMpqLhJtzCCSGQSPzNNczVVPVzSV
WwpllfslqfhffLwhfJpJlqlwdBmZnrdFHBFBBmNHFsFmdZmn
jZfQZnZfnbRfjCnfbSSmVpqmNmVpCqlhCqqPpP
MdJMwMvvLDssLtFMsMtLDsvvDRmmmPhWzWzphpmqDVzPDWNp
TsLdMrvRtLJtGdtGRRtFTBjSBrScnSZjnbcgQgHfnB
RZfmlRlWJmWLLRscrslJqvvMdVwmddvPddQPVDdDwz
GStFbFCbntbjNnjFhFvdHfhzHfzzQdMHwPdD
BSGpFbbjbNjnNNFSbRsLlWqgrZrfRgsBlg
ztHczmrmcNNzHsPSTwsPHSQPQT
CFCRjlvbClCjBdPDFQdwBsqn
llbRgjClJCVVMMCssfmNZWszrNgzGL
mmFldllVlmtdWFvPPFBcSSBW
DZzZGzZswQZHwQZjZzWWTSSvjSdvPvvWjJTS
DpQQggwzZGdmbCldgVgf
PJJvhqzVGbTFqzqbbGTlLmrtrZMnnZnntlJnrD
fNwRcQBCRNddNgLtgDnttqrMMtlr
RfRdNWQHcqHscdfRdGPFbFPpvpVWWzPzVS
DRgjZRRDggTfjfRvwWzHGGHPWDswvv
dhbmpcCmchgCpsGzWPdVGvWHwP
hpMMMpCQMnChFgNRQffTRrSN
gfqPCHWtPMMjCtffgjQWGLvGdZcdLLGZcLFGZBWG
pJTDsnnnvBjnFwvj
zJRpTbNrTSppRVblgbljMgMfCfbC
fGrGwqggtbVmtzbf
CTMjNQcJjJTBNCjMNZFNBcCZHbmWZHVLZDDWVtDzzbVmlV
hMvTcNMFMhQjTTBFBNMhwpspwgnGtvtnSgdwrRpG
RfFdqPdMMGPVgWmNVN
QwrTsbnSsSQpwlSSbNNWDmGLVjjmLWwNVB
rpcclTCprmZQSbprSTpRRRfqMfHHCHfhMhvFJM
LnJJsMtLbzsPPVPJbrTBlTWlfRfqnTrrlr
VDHVQNFGgNTrSjSBjq
CHFHGmvDGdZZGCQZVDgDHVbwLLwtMwwmJLJbLPPMbczt
qNNNBllFBzFjjzwGqGgLrWgrtQjdmmtQmQpp
ZMHJCPhMZRsRCsCPsSJZLmQdQgrtQwQwQZwdWg
CnMPbbRbsPhCnbfhMPRPllnFGqwTTFzTzNvBGBGc
wZWlBFZQgBzTzpZwBlVpzWBWnNMmnMvMcMJMmLGnVmqLqGMq
PdSDfJbCHsHHdJjsRRhjjPjmLqnnrLMLcrnLvdLMNccvGn
tSJtSCtbJhDhtzlFQZlTZTFp
TNqZDqmMDZNMFSGHjSGBRBdN
CrrwVwsPjjBHddPf
rpWggQVspQWcgtLwcHZZzDDMLDvvnnMzDM
lWrWmPwmGlZwZjdLZLzV
cFcDJhJnmqBqDCRpZzVLNsFLjLzdds
qJchTDCBHDWglmrfWPHH
RgLRnTJWnfHDcQQBfg
bZpNwdwbdMvVPsHHJMQfSSfP
mVbdNNdrbCzZbdZvbWTGrhqjTJtRWttRjq
TMtqqBJLrwqrZPlHHGhGnlBhzv
bFgNcpDRnpgggjCzvWDWhQhQWQHHvz
jnnVgjcgcTZMJqJVtT
dVSjmdHrfGPddrQgstFgzsQfsMFQ
hvJJCCJDcCtwBVFQzzBD
RWCnTvWTLRnJJLJllWhTLSprVdNZVGHGNGGnrdGSZH
gvMSHFZtBBMBMFZHzjnqLsLGMCzRWWMn
QJmDrhbNDbJfPQhDmQPRLszRlnjCzzWqrRnlsL
PcJVhJbJJNcNDmfDmjJmbhTfBvpwVSdggtgvgSFZwgvtgpdZ
PBClRHHClRlFljllZSBBBllppVGDLpZVVVsGpmGcNDpGLL
MvNwnbMwccVsswDG
MqnNbzMMrQfnqtttqfQWQQnRdCSHgHPglRFBRWlHjWRlCW
lldwdfSBWphHBggZghFs
DjDbDVRzDmLRzRLGJjPssrLZPhdshFHrssTZ
mvddMzvmmDDvvwQqWftCfqWqfM
gpTTwNWGWMSMgJjnvpvvJbJppn
lQvmLFdfrQzRFctlrLdRLVPnhPPbVDPDfjnVbfhJjV
FLFqccvmmtcQtrmQccRFLlRLSSWBSgTWNwsggqMBsqWGHMNG
PjPtVQrPVjrVPLLDQVFLTTWWqbSZwRwzqwSbSbbbwFSq
lBnGJBnfflRRNZwbqb
HJMGgmfpRMHGGdgncJHLDjjtVDQctLCvQCjTtr
VvmvjRGwRwvhmhRvvvVCCTTJjfWqfDMMcJlcCD
NpNbPfpSnngZbbLMFJWTMlLFqJJDMD
bNSfdSHQZgVQzwhhvRmQ
MhmHcDhChhcPVMDPDPQdFhQHnbNpZbZnprnrmNnjNbsllbnp
WWqGCWSCzsGbbGNgjN
LzwqBLSvwJCLPVMVDLdhMP
mNVLLffSLVWdZCcFZCZrSbGr
glvcwszTlsRDrHQCZFCvGH
gTBRlJnwhzgTgsTnggslsJRTpLNmjmNNcdVLdhfpLpdLVmLc
pCgfDrDrgccfppmDnhHMGqGbpHHSqzGLlqHS
tFtjQRPFFZRVNRcQGbLzLFMSGzSbWLqH
QRNTZjvjTTwtwNfmcTgfnCgnnBhm
hcPBhqPzqWPccHWHHWqnPdssPVfFFmZDnVDDms
NSLNCTRQZndRmDfnRD
QSGTGbjTSTJHBlbZZBbh
dgcWgVgWdvZSbbRtjLRZZZ
MMDPPfTnPTQrFDMpHzmmLztLnsszRtwbtS
rDfDqfHTpCSJqlCCGq
bjsgllstBbpNpslBpdBgqljgGwzJzDzwLGGrwLQQdJDwGhQh
nncmnmHHnmWRWmPfJCnvPRMrzvDhZZLGQwhDLhhMzZZZ
mffccVHRRPTTNlpNbNjJVslJ
DgPstgPtgPNNcjQQrtPJJCRSZTwSGJZZCZCJGD
dHVvpzdBBhVqzWqvhvHdzGSZlTRCSRJrwSSCwJCWGT
zpvVVqMBrzqrhFBvjbNPcPLnjcQtMcnj
gBcmTCFghhCCBnBhWWwFbwLdwHFMLMdp
LVzlZzPPMMzWWrwH
ljqjsGlZPPqqlVsPqDVqjQQctNTnRcNLtCNmmnRTRthBGG
LPRrrBNNjLBRJNdrGPRBfBrLwFqmDbdbTbTgmmgwmttFwtmH
QQcVvnQphlWsCQCCVpnvptTJgbtqwHDwbJtJHFsTHw
ppcJVQvpvMVMCvQZQVVZCCSRZPSjNRRZBPPPPzLjSLGf
MLtRnjQsRMJcDQJnSrsfqVVvGwbbbqgggg
WBFCNlFFFhFBlCHbplFWdpWZfVqPPwqTGdqTGvwrPVvTqvTr
HClCHzFzFBhmnjtQzMMSMnbD
sVnMCsdlMRcMFBGz
JvwwgrJDfgDmmggQrhNfhQQftjFrGRRtZFGBRZFHzjGcjrcj
PBJJvgDPNllPddVCPl
fmmRSnfnMnFSmMmmzTDSBFHtlJJqHJJqdHQdTCdtCCdt
WggGpNVVgWdwwHQtlGlC
hjbWppbLbLZLjVPPjPLSRRMvDlmSzDzBSnBFZf
nVttMPnPLjnJLjcnPVCjJJLcssfggBNlffgcNsWTcGcgNsBF
HQbwhmDrRrgFsWlQGNls
pZdbGzGrGpVttPLttv
LLbMrMHLDdWhmgbqqt
jGSQZQTpQGVVRSlQMQRljZmgmJBSvggvBWhJmJWvddmt
VjlQFGMVrFFrDrPw
DZVDwGZlJlVlwZVDzNdqfjMDnjqzNnWf
pmtpLRQFhSFpmpRgRtHNFznNdqWBjzWfnBjMWf
rHRrhStppHdJcGJrrssCsV
pgQqHwgPcPCddCjdWtdp
VfZGVFfNVhZhzjjjLz
fNNBBnGVNfBfRSRjBRQHJQTwJcJTgHPwTngr
MZdlzWzthMgrwmGmqZNqNs
VvJQJPVDBJQThwwNsRqsvRsHHm
BDQQPTnDDBQQBVfTBQPdFctzzdtztMMtnhcWcd
LjWjDShflZRRcZzfHH
srNwQPBsrVRhNmRGHzmM
rBdgQTrhdPndQTrsQQsrPwnTpLLCWDpSCLtCnvtSWpJjDCvl
gSlvDwCvcmcTQTFtRMjWHFVVHwtj
rbsphZZzBshGZssMffTVRFfFpWpfTH
GZNhZBhPBzTPNLDcDlCDCJNmlg
smZjGfvjbWWffQtf
dwRrdlVdDdgDbNtgcgQSNStQ
FdFVwdblFlzVrlwrTlndZHHZGhmLhhssjHhMjnjq
QFvQVFLLgVrFLBVgGhTtllPvmHRRGbTm
hDCCNCNCJNzWDZnqJDzSNCTnbRttHGRnccbPRtmmlmHc
qJshNMCNdVFVfsLB
FcLZZPFjdZcZMPcRjcRTgbpJlwbbTlmdTlGlwD
nrrNrHWBNSWvBqvvrhBqzStrgGnnmbwsbbJbwwJnmwmgJTlD
BCrrNvqWvSQPcCGZZRQQ
vPwcJblJzJbJcJFcwBSvJNdWRLtdsddGWWddWRWsMF
mDZmmDZDHVhfmjZgjVDfhTZHtsNptRsMntnWdsMnGtRntG
mhQrQDDhgqTTNfhmVQVBrPlBczSJbbCbCCPPvb
ZjbjLlbZjGqsgJTfHggrVvlB
tFDRFRnMFnnWtDdMdDRhzHfTJhJhffHvHTBHTgcfJV
nztDtdWzCCMSptSdFRRswZjsLbjwZmwqwGqpQV
vnvmmVnmVbrBJlzgWQWVNFzNHV
MwSjZhSwPjMwfDRzgWlNpWvHlgNNNP
CfSZjSfftwZDChDRSnccnrvBbbGrtBvctr
LCBRQRBQwRrCVLVWSrCSwCptzvhthvGGhdHzwppTTddv
mFnJJmnmFFFfPLNNmqqNJDpGnGtbHTtHvhnHbzvHvpGv
lMMPLqDmNMVSjjgMCS
zzPzbLjHLjfQPQHwwjddFNsNSJjDMsdNMFsC
BqqtmgDhcqdSFCdsqddF
GtcmrvhgcZlvZtBhtVgrvrvtnWzDnQbfnwlfWWRHWbbwzHRL
JfWHWZcMMdDLMPjRnCJjRbFgnblF
ShtBTSmBhTtqtfmqSTNvmjVjnFbFnnlrlqgCnrFnVg
vfzTTthppmdzPLHLWdGZ
tdvrvGgGTSScnHcjcg
zLLVfzPPcDZnPjSPpD
LfffNFLNlNbJwrctthWqNdNq
NdjJtfVNZnnFFdtfGfFNcvpbMDbzdcTbbzpvmcDR
PHMSHCHHWrRCvzDzDChT
BqPWSHwllSQWrLHQHPqlBBNfttZMjFQfjGtZtNjJJjnN
CpZtMCMQQpCVWjMDVjPVQsWWqJJhbTcddPlfhTRqchcJblhh
NwDSGNmGRccqNJfT
SBSSmgrrgGHnvSzwGVWDCzMCpLZtMsstLM
sbjHQsBlBQrrGjQjBqCRSnSCpnfngLnFhJngFfSP
zHVctHDcZtdJffnPpcSpFn
ZdwNMztdvzVdrqblvWsqHvBR
jPdjFPSbVDMMbqZzQWzQ
hFRrJlpprGhtlJGQzmCRmZBWQCHRQR
vThNplJpNhltNNlvcGDvwVFgnPwvSgPSSfjS
DhDTPQpTDmQbDQrrrWtWPJNNrrsJ
qqGjgwCgVRjMSRwMMGRGqjwvsNJJBZtrstvNBvHWHJvL
VqqgfjzfgfFGVjRggCGznhlbTpQchcshpdFlnDbn
DpTQTBbCZQVJQZJjrFllGdlvMPlMLqGBGvLl
hmnWHWWNzzmHsmWRlGGpdLgLHGlqvgqg
RzcWRhRnRnfmswfwtzzRWrDTrrFCQTCpQpcCrjjQCp
HLvpHvGcBTDFznvfqT
hCPQbPZPbjSbwwjCPChSClJJfzqTggTFDfsJngDg
StqmmZbdqrQmhQrrhZWcRcGBpBHWVcLctMWp
dNnRNbRdbRJMBMBVVThn
rNrsLNscFsCDjpwTMgBGWMGjJjWBVJ
wNcLpqHNsCprsfLFsHwRvPSSPRZRtRQSqtQPmP
PPhGfbthhBDVsTDtDqRR
mCmSNmqpcqjjrCScWRsZDpHsDQRZQDZDss
CcWzNmccrjjvqBGzzdPGnv
SDRmCSFfcSFFcfDmDBFSCfdVJhpzZjNJTNzRTvjzjhzNjTtZ
ngGsltrMWrblNpNTJJplJN
PGGnGsWngrGLQHHtHHHgWsHSBLqqfLcqBdVdcCDDBFdCDm
VPjGwhwVPhrnqhzJmQvQTQvmzBzw
ZBDBRbLLdtfRLlddLlCLCZMgmFJQFDcvzMQmgMzzJJFJ
LHLWltHlRZCtBVhVVHPjGSpphp
JqhlhdnnmfRVVSpzWLjzVLGpvB
stQtFTTrsZQPFQNNDtQgLzzSLvjvLGLBGSZGGWJv
DDDFFgDPbTwbTTJMCMcbCqqmmRRCnb
JbDWPDPPJJDMDjHPZHGbHGVZTBhrzBpdzszdTTphdNdWdrpv
RmRRqllqffwFtqwLCsqTNvpCsqCNqvdN
fmfLmStlnnfnRtfcnQbbjPjPPggZGVsMQMbb
WJggvGDJSwWgSfgvfSMGqqQHBcPjcHChcQBCssDHCTTQ
mlRnbrnbnltblwdnnpbLRdCCjCTHTjPTTsQcTrHHhCcj
bFLbdmzRpvSwfFFNWN
BHnDnQHnHMWLwzWPzD
dmlZCrdqLZzZVZJM
tRRtdlLCjLmqCRsrSLrvvRQNFQnbgRTQQNHTBbGQQh
ZrQPQWCrJnPdQSNTmBJNTHGHJN
zhFRfswjwhhsFttfsfvQftRtLTzmBTHGTBmzMLHHLmGHNTTS
hQhwqVjQwsdggrZZCWVl
VjfnQgVQjblChfjVJlbzLtrSLlTGtztHTtsTGH
DDqWQDQMWmDwWNwcqdWvpSrtLpLsptMprMStstMz
vQcddRdRvWcwWRmmmmddZmmfVnnngJJbZnCBnBhhFbhCgJ
gVgDnnmJdQVdJJgtgDjBsBhsBSPRSRRSSwccSbSqwPcCPcSC
HrQHlHFpQfTHzzWzwScPPCRfLbPSfCSR
TTQlZNTzlZNMWvrZMlpnhnVtnDDnVNtVJnjmhg
MCmmssFnZJcNNszfpvvrpvJzvwpp
BRRRWQWbSRGGRTTtZHWSqTrvDfgfdfrrwrDgfbvfzfrd
jRBhWRWTSRttQBZMNchNCsmFMchP
GBDncllqcSlNFZWBFWPjHVbw
LQphJlJzLCwPjHbpHZvV
hzCMJLMzTsrdrszQCCCTCQCDlqqnNmggqfGmgdmGgcmSNt
hFVVbqJsqhcnBRTRGBTh
lwdDpmzdNznzZBgGRRjR
HdmvNvSCmDmwNDFrMJMqJFCRfsbq
ctnbTcFTnbwSSfrrMLRhpJLMRdpwdJJR
vdGCVBmGVHPLBRWhpRLJJZ
VmQPHqvsPdlQsVHDftnlFTbffnbttfTF
LBJZHrhLThHddcMLVtcMcL
CPMNFDDMpGqFjjSPDPDqdvmdtQgVQQcQWcQgQQsj
DzFDFMRSFPSGTJJTJBwwRhBw
dpldqlqlRppFTHpbjbnLRLVnnGfjtG
NNJTcmhzvJQNgMJBwcGtjtGbttfhtsGGnhnt
rzcwmgvcvrBNvvmMgvcBzwHPCTWWprqPHqTFWdPCWDTF
BNllDRTNqDNvNDDLBcDvBCLVJrVdJdtrnrCHggtrdd
mppFMFjpMFZQZQGjFCdgrCrCdrvVGtJJCC
PZsQmfPphvPjSsjmPjfZllBwcNRDNcDqNNWbTclS
fjqZBSDSDwwsQwCDND
rrdMdjVWtTTPslsslFLTLCsJ
rvPWbvcmHjmdPbHvrvBHgqRRgqHGgfZGfHRS
ggTQgsgwFrTrggbMTvSdmjfCmmQDcmqjDjmc
nLZnRhNZnnNHZhZVStCcDqjcqmjSjH
RWGNnhzBnJJRRWNRBNZNLZhFMTFPvrTrTlsggPwSlFMWTw
RNmnPRnLGcQmzBQpHHjTltjtlfgspbsq
CZvCJwZMMCCMdFVcwJJsgTTHfsTlbfbgbT
SSVFhWCZdSCcWCcWdrvhzmnnnLNGDRDNzzLNGz
jPwfPwNfFpFNQpDjdMcjcrdddDHD
tzsRsGRLzhLhvqvhHMlqqV
LRBnRBGSnBSGsGSGmGtBJCmnNWZpPpTNPMwQMPNJFZTTNwWT
PCrStRPSPvZQcZPvqvfjSRWFFNFJFLZTTJTTVZFFGLFF
DlpBzBntHDzhlpGJVHLwTMFLVLTL
gptBBdgzpsBbpQvvPQPRqrdcCC
"""

linhas = amostra.split("\n")

linhas_sem_vazios = list(filter(lambda x: x!='', linhas))

lista_com_todas_as_linhas_divididas = []

for linha in linhas_sem_vazios:
    lista_metades = []

    numero_de_caracteres = len(linha)

    primeira_metade = linha[0:(numero_de_caracteres//2)]
    segunda_metade = linha[(numero_de_caracteres//2): numero_de_caracteres]
    
    lista_metades.append(primeira_metade)
    lista_metades.append(segunda_metade)

    lista_com_todas_as_linhas_divididas.append(lista_metades)

lista_caracteres_iguais = []

for linha_dividida in lista_com_todas_as_linhas_divididas:
    primeira_metade = linha_dividida[0]
    segunda_metade = linha_dividida[1]

    for caractere1 in primeira_metade:
        for caractere2 in segunda_metade:
            if caractere1 == caractere2:
                lista_caracteres_iguais.append(caractere1)
                break

lista_caracteres_iguais_sem_repeticao = list(set(lista_caracteres_iguais))

lista_valores = []
lista_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for caracter in lista_caracteres_iguais_sem_repeticao:
    for letra in lista_letras:
        if caracter == letra:
            lista_valores.append(lista_letras.index(letra)+1)
            print(letra, " ", lista_letras.index(letra)+1)

soma_valores = sum(lista_valores)
print(soma_valores)