#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Note: Since I was under some time constraints, I did not have enough time to complete automated tests. I did run tests manuallt of the functions and I was convinced that they were working bug-free in my script. If you are interested in helping this project, please consider writing some tests.

import unittest
from beagleTM2_browser_helperCode import getIntersection
from beagleTM2_browser_helperCode import writer # function to help in debugging
from beagleTM2_browser_helperCode import reduceResults
from beagleTM2_browser_helperCode import getLogTransform

# Run automated testing:
# python3 -m unittest beagleTM2_analysis_i.py

class test_beagleTmApp(unittest.TestCase):

	def test_Intersection(self):
		"""Check that correct a correction intersection is reached."""
		self.assertEqual(getIntersection([1,2,3],[2,3]),set({2,3}))
		# end of test_Intersection
	def test_writer(self):
		"""Check that writer is outputting some text. """
		self.assertEqual(writer("ok computer"),"ok computer")
		# test_writer()
	def test_reduceResults(self):
		"""check that the upper half of input list is correctly copied to another list to be returned"""
		in_list = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
		a_list  = ["a","b","c","d","e","f","g","h","i","j"]
		b_list  = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj"]

		out50_list = [0.2, 0.3, 0.4, 0.5]
		aout50_list = ['c', 'd', 'e', 'f']
		bout50_list = ['cc', 'dd', 'ee', 'ff']

		self.assertEqual(reduceResults(in_list,a_list,b_list, 0.10, 0.50), (out50_list, aout50_list, bout50_list))
		# end of test_reduceResults()

	def test_getLogTransform(self):
		"""Check that the log transform function is working correctly"""
		in_list = [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
		base2_list = [-6.643856189774724, -3.321928094887362, -2.321928094887362, -1.7369655941662063, -1.3219280948873622, -1.0, -0.7369655941662062, -0.5145731728297583, -0.3219280948873623, -0.15200309344504997]

		self.assertEqual(getLogTransform(in_list, 2),base2_list)
		# end of test_getLogTransform()


# Some data for future tests.
data_dic ={
  "title": [
    "Use of personalised risk-based screening schedules to optimise workload and sojourn time in screening programmes for diabetic retinopathy: A retrospective cohort study",
    "Identification of a novel picornavirus related to cosaviruses in a child with acute diarrhea",
    "Use of personalised risk-based screening schedules to optimise workload and sojourn time in screening programmes for diabetic retinopathy: A retrospective cohort study",
    "Uneven modulation of the annexin 1 system in osteoblast-like cells by dexamethasone☆",
    "LOTUS: A single- and multitask machine learning algorithm for the prediction of cancer driver genes",
    "Thoracic epidural analgesia: a new approach for the treatment of acute pancreatitis?",
    "Deletion of a xenobiotic metabolizing gene in mice affects folate metabolism",
    "Crystal structure of tri­phenyl(vinyl)­phospho­nium tetra­phenyl­borate",
    "Hepatitis E virus is highly prevalent among pregnant women in Gabon, central Africa, with different patterns between rural and urban areas"
  ],
  "abstract": [
    " BackgroundNational guidelines in most countries set screening intervals for diabetic retinopathy (DR) that are insufficiently informed by contemporary incidence rates. This has unspecified implications for interval disease risks (IDs) of referable DR, disparities in ID between groups or individuals, time spent in referable state before screening (sojourn time), and workload. We explored the effect of various screening schedules on these outcomes and developed an open-access interactive policy tool informed by contemporary DR incidence rates.  Methods and findings Scottish Diabetic Retinopathy Screening Programme data from 1 January 2007 to 31 December 2016 were linked to diabetes registry data. This yielded 128,606 screening examinations in people with type 1 diabetes (T1D) and 1,384,360 examinations in people with type 2 diabetes (T2D). Among those with T1D, 47% of those without and 44% of those with referable DR were female, mean diabetes duration was 21 and 23 years, respectively, and mean age was 26 and 24 years, respectively. Among those with T2D, 44% of those without and 42% of those with referable DR were female, mean diabetes duration was 9 and 14 years, respectively, and mean age was 58 and 52 years, respectively. Individual probability of developing referable DR was estimated using a generalised linear model and was used to calculate the intervals needed to achieve various IDs across prior grade strata, or at the individual level, and the resultant workload and sojourn time. The current policy in Scotland—screening people with no or mild disease annually and moderate disease every 6 months—yielded large differences in ID by prior grade (13.2%, 3.6%, and 0.6% annually for moderate, mild, and no prior DR strata, respectively, in T1D) and diabetes type (2.4% in T1D and 0.6% in T2D overall). Maintaining these overall risks but equalising risk across prior grade strata would require extremely short intervals in those with moderate DR (1–2 months) and very long intervals in those with no prior DR (35–47 months), with little change in workload or average sojourn time. Changing to intervals of 12, 9, and 3 months in T1D and to 24, 9, and 3 months in T2D for no, mild, and moderate DR strata, respectively, would substantially reduce disparity in ID across strata and between diabetes types whilst reducing workload by 26% and increasing sojourn time by 2.3 months. Including clinical risk factor data gave a small but significant increment in prediction of referable DR beyond grade (increase in C-statistic of 0.013 in T1D and 0.016 in T2D, both p < 0.001). However, using this model to derive personalised intervals did not have substantial workload or sojourn time benefits over stratum-specific intervals. The main limitation is that the results are pertinent only to countries that share broadly similar rates of retinal disease and risk factor distributions to Scotland.  ConclusionsChanging current policies could reduce disparities in ID and achieve substantial reductions in workload within the range of IDs likely to be deemed acceptable. Our tool should facilitate more rational policy setting for screening. ",
    " Diarrhea, the third leading infectious cause of death worldwide, causes approximately 2 million deaths a year. Approximately 40% of these cases are of unknown etiology. We previously developed a metagenomic strategy for identification of novel viruses from diarrhea samples. By applying mass sequencing to a stool sample collected in Melbourne, Australia from a child with acute diarrhea, one 395 bp sequence read was identified that possessed only limited identity to known picornaviruses. This initial fragment shared only 55% amino acid identity to its top BLAST hit, the VP3 protein of Theiler's-like virus, suggesting that a novel picornavirus might be present in this sample. By using a combination of mass sequencing, RT-PCR, 5' RACE and 3' RACE, 6562 bp of the viral genome was sequenced, which includes the entire putative polyprotein. The overall genomic organization of this virus was similar to known picornaviruses. Phylogenetic analysis of the polyprotein demonstrated that the virus was divergent from previously described picornaviruses and appears to belong to the newly proposed picornavirus genus,Cosavirus. Based on the analysis discussed here, we propose that this virus represents a new species in the Cosavirus genus, and it has tentatively been named Human Cosavirus E1 (HCoSV-E1). ",
    "BackgroundNational guidelines in most countries set screening intervals for diabetic retinopathy (DR) that are insufficiently informed by contemporary incidence rates. This has unspecified implications for interval disease risks (IDs) of referable DR, disparities in ID between groups or individuals, time spent in referable state before screening (sojourn time), and workload. We explored the effect of various screening schedules on these outcomes and developed an open-access interactive policy tool informed by contemporary DR incidence rates.Methods and findingsScottish Diabetic Retinopathy Screening Programme data from 1 January 2007 to 31 December 2016 were linked to diabetes registry data. This yielded 128,606 screening examinations in people with type 1 diabetes (T1D) and 1,384,360 examinations in people with type 2 diabetes (T2D). Among those with T1D, 47% of those without and 44% of those with referable DR were female, mean diabetes duration was 21 and 23 years, respectively, and mean age was 26 and 24 years, respectively. Among those with T2D, 44% of those without and 42% of those with referable DR were female, mean diabetes duration was 9 and 14 years, respectively, and mean age was 58 and 52 years, respectively. Individual probability of developing referable DR was estimated using a generalised linear model and was used to calculate the intervals needed to achieve various IDs across prior grade strata, or at the individual level, and the resultant workload and sojourn time. The current policy in Scotland—screening people with no or mild disease annually and moderate disease every 6 months—yielded large differences in ID by prior grade (13.2%, 3.6%, and 0.6% annually for moderate, mild, and no prior DR strata, respectively, in T1D) and diabetes type (2.4% in T1D and 0.6% in T2D overall). Maintaining these overall risks but equalising risk across prior grade strata would require extremely short intervals in those with moderate DR (1–2 months) and very long intervals in those with no prior DR (35–47 months), with little change in workload or average sojourn time. Changing to intervals of 12, 9, and 3 months in T1D and to 24, 9, and 3 months in T2D for no, mild, and moderate DR strata, respectively, would substantially reduce disparity in ID across strata and between diabetes types whilst reducing workload by 26% and increasing sojourn time by 2.3 months. Including clinical risk factor data gave a small but significant increment in prediction of referable DR beyond grade (increase in C-statistic of 0.013 in T1D and 0.016 in T2D, both p < 0.001). However, using this model to derive personalised intervals did not have substantial workload or sojourn time benefits over stratum-specific intervals. The main limitation is that the results are pertinent only to countries that share broadly similar rates of retinal disease and risk factor distributions to Scotland.ConclusionsChanging current policies could reduce disparities in ID and achieve substantial reductions in workload within the range of IDs likely to be deemed acceptable. Our tool should facilitate more rational policy setting for screening.",
    "We tested whether glucocorticoids modulated osteoblast expression of the annexin 1 system, including the ligand and two G-coupled receptors termed formyl-peptide receptor (FPR) and FPR-like-1 (FPRL-1). In Saos-2 cells, rapid up-regulation of FPR mRNA upon cell incubation with dexamethasone (0.01–1 μM) was observed, with significant changes as early as 2 h and a more marked response at 24 h; annexin 1 and FPRL-1 mRNA changes were more subtle. At the protein level, dexamethasone provoked a rapid externalization of annexin 1 (maximal at 2 h) followed by delayed time-dependent changes in the cell cytosol. Saos-2 cell surface expression of FPR or FPRL-1 could not be detected, even when dexamethasone was added with the bone modelling cytokines interleukin-6 or interleukin-1. The uneven modulation of the annexin 1 system (mediator and its putative receptors) in osteoblasts might lead to a better understanding of how these complex biochemical pathways become operative in bone.",
    " Cancer driver genes,i.e., oncogenes and tumor suppressor genes, are involved in the acquisition of important functions in tumors, providing a selective growth advantage, allowing uncontrolled proliferation and avoiding apoptosis. It is therefore important to identify these driver genes, both for the fundamental understanding of cancer and to help finding new therapeutic targets or biomarkers. Although the most frequently mutated driver genes have been identified, it is believed that many more remain to be discovered, particularly for driver genes specific to some cancer types. In this paper, we propose a new computational method called LOTUS to predict new driver genes. LOTUS is a machine-learning based approach which allows to integrate various types of data in a versatile manner, including information about gene mutations and protein-protein interactions. In addition, LOTUS can predict cancer driver genes in a pan-cancer setting as well as for specific cancer types, using a multitask learning strategy to share information across cancer types. We empirically show that LOTUS outperforms five other state-of-the-art driver gene prediction methods, both in terms of intrinsic consistency and prediction accuracy, and provide predictions of new cancer genes across many cancer types. ",
    " This review article analyzes, through a nonsystematic approach, the pathophysiology of acute pancreatitis (AP) with a focus on the effects of thoracic epidural analgesia (TEA) on the disease. The benefit–risk balance is also discussed. AP has an overall mortality of 1 %, increasing to 30 % in its severe form. The systemic inflammation induces a strong activation of the sympathetic system, with a decrease in the blood flow supply to the gastrointestinal system that can lead to the development of pancreatic necrosis. The current treatment for severe AP is symptomatic and tries to correct the systemic inflammatory response syndrome or the multiorgan dysfunction. Besides the removal of gallstones in biliary pancreatitis, no satisfactory causal treatment exists. TEA is widely used, mainly for its analgesic effect. TEA also induces a targeted sympathectomy in the anesthetized region, which results in splanchnic vasodilatation and an improvement in local microcirculation. Increasing evidence shows benefits of TEA in animal AP: improved splanchnic and pancreatic perfusion, improved pancreatic microcirculation, reduced liver damage, and significantly reduced mortality. Until now, only few clinical studies have been performed on the use of TEA during AP with few available data regarding the effect of TEA on the splanchnic perfusion. Increasing evidence suggests that TEA is a safe procedure and could appear as a new treatment approach for human AP, based on the significant benefits observed in animal studies and safety of use for human. Further clinical studies are required to confirm the clinical benefits observed in animal studies.",
    "The mouse arylamine N-acetyltransferase 2 (Nat2) and its homologue (NAT1) in humans are known to detoxify xenobiotic arylamines and are also thought to play a role in endogenous metabolism. Human NAT1 is highly over-expressed in estrogen receptor positive breast tumours and is implicated in susceptibility to neural tube defects. In vitro assays have suggested an endogenous role for human NAT1 in folate metabolism, but in vivo evidence to support this hypothesis has been lacking. Mouse Nat2 provides a good model to study human NAT1 as it shows similar expression profiles and substrate specificities. We have generated transgenic mice lacking a functional Nat2 gene and compared the urinary levels of acetylated folate metabolite para-aminobenzoylglutamate in Nat2 knockout and Nat2 wild-type mice. These results support an in vivo role for mouse Nat2/human NAT1 in folate metabolism. In addition, effects of the Nat2 deletion on sex ratios and neural tube development are described.",
    " The title ionic salt, C21H20P+·C24H20B−, crystallized with two independent vinyl­tri­phenyl­phospho­nium cations and two independent tetra­phenyl­borate anions per asymmetric unit. These four independent moieties contain nearly perfect tetra­hedral symmetry about their respective central C atoms. In the crystal, there are no π-stacking or other inter­molecular inter­actions present. ",
    " Hepatitis E virus (HEV) is highly endemic in several African countries with high mortality rate among pregnant women. Nothing is known about the circulation of this virus in central Africa. We evaluated therefore the prevalence of anti-HEV IgG in samples collected from pregnant women living in the five main cities of Gabon, central Africa. We found that 14.1% (119/840) of pregnant women had anti-HEV IgG. The prevalence differed between regions and between age groups. In 391 newly collected samples from the region where the highest prevalence was found, a significant difference (p< 0.05) in seroprevalence was found between rural (6.4%) and urban (13.5%) areas. These data provide evidence of a high prevalence of HEV in Gabon, providing indirect evidence of past contact with this virus. "
  ],
  "pmid": [
    31622334,
    19102772,
    31622334,
    17254556,
    31568528,
    27141977,
    17961509,
    25484719,
    19102767
  ],
  "journal": [
    "PLoS Med",
    "Virol J",
    "PLoS Med",
    "Biochem Biophys Res Commun",
    "PLoS Comput Biol",
    "Crit Care",
    "Biochem Biophys Res Commun",
    "Acta Crystallogr Sect E Struct Rep Online",
    "Virol J"
  ],
  "year": [
    2019,
    2008,
    2019,
    2007,
    2019,
    2016,
    2007,
    2014,
    2008
  ],
  "references": [
    "[20536486, 17627978, 8719346, 28224275, 16026382, 30559224, 24599419, 19940227, 21792613, 28840258, 28423305, 21562322, 23055834, 2062510, 24682180, 28684650, 25510978]",
    "[12764516, 15825143, 20536486, 8719346, 15702043, 8380619, 12409408, 18398449, 16032716, 9785211, 14624234, 19033469, 1658159, 16381856, 17942560, 18420805, 17686542]",
    "[20536486, 17627978, 28224275, 8719346, 16026382, 30559224, 24599419, 19940227, 21792613, 28840258, 28423305, 21562322, 23055834, 2062510, 24682180, 28684650, 25510978]",
    "[11917092, 8747277, 20536486, 10956650, 12369789, 8719346, 10359570, 7961821, 8898757, 12368905, 12401407, 9536335, 9664068, 10499489, 16973129, 11159197, 1533045, 15238251, 11815387, 12639897, 16720734, 10092818, 14662730, 1581117, 7512342, 9435302]",
    "[10647931, 21376230, 20536486, 8719346, 18948947, 15192155, 2274789, 12893203, 6095109, 17611206, 14993899, 24071849, 27899578, 23539594, 23770567, 22960745, 23945592, 22759861, 23340843, 24390350, 22904074, 23383675, 29625053, 26635391, 24183448, 25690659, 27911828, 22460905, 25501392, 27333808, 21977986, 28126037, 29236960, 27811361, 28399410, 28564583, 26130958, 26201458, 27004405, 25954303, 11809771, 26074087, 29069470, 29059173, 28642997, 30618016, 26496030, 29168346, 26811690, 28771744, 30405814, 26910837, 24608975, 25320087, 29960071, 27022003, 25128227, 25335771, 27044843, 25569148, 28607512, 18988627]",
    "[22885331, 23622135, 23896955, 22058144, 23203897, 25685727, 16707751, 18191686, 16633121, 16607683, 2252994, 18852942, 19125434, 18086987, 17327743, 16871070, 17117138, 17589385, 16460474, 16521220, 17646505, 9310001, 19934868, 24314012, 10969322, 17717251, 16480459, 11908096, 26604652, 17113358, 18854796, 22100213, 23100216, 7587228]",
    "[15627487, 11005799, 20536486, 10767335, 8719346, 8719346, 9170149, 10667461, 15084249, 7717963, 7598738, 12815365, 11553922, 11034085, 1329759, 17295418, 17063929, 14517345, 15523664, 16680433, 17177317]",
    "[]",
    "[12740830, 18287615, 18287603, 20536486, 18192058, 8719346, 16705571, 18297720, 9272579, 9625307, 8355020, 16254969, 1940876, 9311635, 10504860, 16257426, 8915876, 7485684, 14981755, 18098159, 16413822, 17728471, 17336401]"
  ],
  "keyword": [
    "['with', 'between', 'and', 'is', 'in', 'countries', 'with', 'rate', 'among', 'is', 'the', 'of', 'this', 'in', 'we', 'the', 'of', 'in', 'from', 'in', 'the', 'main', 'of', 'we']",
    "['with', 'and', 'virus', 'is', 'in', 'with', 'rate', 'is', 'known', 'the', 'of', 'this', 'virus', 'in', 'we', 'the', 'of', 'in', 'samples', 'collected', 'from', 'in', 'the', 'of', 'we']",
    "['with', 'between', 'and', 'is', 'in', 'countries', 'with', 'rate', 'among', 'is', 'the', 'of', 'this', 'in', 'we', 'the', 'of', 'in', 'from', 'in', 'the', 'main', 'of', 'we']",
    "['with', 'and', 'in', 'with', 'the', 'of', 'in', 'we', 'the', 'of', 'in', 'in', 'the', 'of', 'we']",
    "['and', 'is', 'in', 'rate', 'is', 'about', 'the', 'of', 'this', 'in', 'we', 'therefore', 'the', 'of', 'in', 'in', 'the', 'five', 'main', 'of', 'we']",
    "['with', 'and', 'is', 'in', 'with', 'mortality', 'is', 'the', 'circulation', 'of', 'this', 'in', 'the', 'of', 'in', 'in', 'the', 'main', 'of']",
    "['and', 'is', 'highly', 'in', 'high', 'rate', 'is', 'known', 'the', 'of', 'this', 'in', 'we', 'the', 'of', 'in', 'in', 'the', 'cities', 'of', 'we']",
    "['central', 'with', 'and', 'in', 'with', 'rate', 'about', 'the', 'in', 'central', 'the', 'in', 'in', 'the', 'central']",
    "['central', 'africa', 'with', 'between', 'rural', 'and', 'urban', 'areas', 'hepatitis', 'virus', 'hev', 'is', 'highly', 'endemic', 'in', 'several', 'african', 'countries', 'with', 'high', 'mortality', 'rate', 'among', 'pregnant', 'women', 'nothing', 'is', 'known', 'about', 'the', 'circulation', 'of', 'this', 'virus', 'in', 'central', 'africa', 'we', 'evaluated', 'therefore', 'the', 'prevalence', 'of', 'anti-hev', 'igg', 'in', 'samples', 'collected', 'from', 'pregnant', 'women', 'living', 'in', 'the', 'five', 'main', 'cities', 'of', 'gabon', 'central', 'africa', 'we']"
  ],
  "counts": [
    "[13, 2, 32, 23, 75, 2, 13, 7, 0, 23, 8, 12, 1, 75, 6, 8, 12, 75, 1, 75, 8, 1, 12, 6]",
    "[1, 3, 13, 7, 17, 1, 2, 7, 3, 10, 9, 3, 13, 17, 1, 10, 9, 17, 1, 1, 3, 17, 10, 9, 1]",
    "[13, 2, 32, 23, 75, 2, 13, 7, 0, 23, 8, 12, 1, 75, 6, 8, 12, 75, 1, 75, 8, 1, 12, 6]",
    "[3, 7, 18, 3, 8, 6, 18, 2, 8, 6, 18, 18, 8, 6, 2]",
    "[7, 8, 28, 2, 8, 1, 8, 6, 1, 28, 2, 1, 8, 6, 28, 28, 8, 1, 1, 6, 2]",
    "[3, 6, 13, 25, 3, 2, 13, 20, 2, 10, 0, 25, 20, 10, 25, 25, 20, 1, 10]",
    "[7, 7, 1, 15, 1, 2, 7, 1, 3, 3, 1, 15, 0, 3, 3, 15, 15, 3, 1, 3, 0]",
    "[1, 1, 1, 8, 1, 1, 1, 4, 8, 1, 4, 8, 8, 4, 1]",
    "[2, 0, 2, 3, 1, 2, 1, 1, 0, 3, 0, 5, 1, 1, 11, 1, 0, 1, 2, 4, 1, 1, 1, 3, 3, 0, 5, 1, 1, 6, 1, 7, 2, 3, 11, 2, 0, 3, 1, 1, 6, 5, 7, 0, 0, 11, 2, 2, 2, 3, 3, 1, 11, 6, 1, 1, 1, 7, 0, 2, 0, 3]"
  ]
}
