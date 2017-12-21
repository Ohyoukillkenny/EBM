# EBM

Lingkun Kong, Xudong Wu, Hongru Zhu, Luoyi Fu, Xinbing Wang  — *Shanghai Jiao Tong University*

![EBM icon](http://www.z4a.net/images/2017/12/21/EBM.png)

##### We build an Evolving Bipartite Model (EBM) to reveals the bounded weights in social networks by launching a case study in recommendation networks.

#### Documentation

1. **Code** file contains codes for analysis in 10 social network datasets, including 6 recommendation networks, 3 scholarly networks and 1 twitter social networks. The download links for these datasets are provided here:

   ​	a. Amazon Datasets: http://jmcauley.ucsd.edu/data/amazon/links.html

   ​	b. Audioscrobbler: http://www.dtic.upf.edu/~ocelma/MusicRecommendationDataset/

   ​	c. BookCrossing: http://www2.informatik.uni-freiburg.de/~cziegler/BX/

   ​	d. Microsoft Academic Graph: http://acemap.sjtu.edu.cn/acenap/index.php/datasets.html


   ​	e. Twitter Social Networks: http://an.kaist.ac.kr/traces/WWW2010.html

2. **EBM-Technical-Report.pdf** is the complete version of our paper for MobiHoc 2018. In this report, we attach additional Appendix B, C, D, E, F to mathematically justify properties of EBM.

#### Further Introduction of Code

1. **Configuration:** Python 2.7 + Anaconda 2.7
2. Prior to run the .py files, please download corresponding datasets from the given urls.
3. We use the code in the folder **Simulation** to run simulations of our model and testify the results for degree and vertex weight distributions in user and item groups.
4. We use the code in the folder **RealDatasetValidation** to validate our observations on several real RS datasets.
5. We provide here a sample dataset file for the BookCrossing RS and the code in the folder **ReadDatasetValidation/BookCrossing** is ready for testing.