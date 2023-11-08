# Influential Node Detection on Graph on Event Sequence
This repository contains the implementation of the Soft K-shell algorithm and supplementary information \& results from its application to real-world datasets. This is the code for paper "Influential Node Detection on Graph on Event Sequence", which is accepted and published in COMPLEX NETWORKS 2023.

### Abstract

Numerous research efforts have centered on identifying the most influential players in networked social systems. This problem is immensely crucial in the research of complex networks. Most existing techniques either model social dynamics on static networks only and ignore the underlying time-serial nature or model the social interactions as temporal edges without considering the influential relationship between them. In this paper, we propose a novel perspective of modeling social interaction data as the graph on event sequence, as well as the Soft K-Shell algorithm that analyzes not only the network’s local and global structural aspects, but also the underlying spreading dynamics. The extensive experiments validated the efficiency and feasibility of our method in various social networks from real world data. To the best of our knowledge, this work is the first of its kind.

### Algorithm pseudocode
We give the pseudocode of the proposed Soft K-shell algorithm here.

```{r, highlight=TRUE}
# Soft K-shell Algorithm
Data: graph  G = (V, E), parameter  β, node property  α(v), use-node-property
Result:  A(v), the overall influence for each vertexes  v

    initialization;
    For all nodes  v  do{
        if  use-node-property  is True then{
            A(v)  ←  α(v);
        }
        else{
            A(v)  ←  1;
        }
    }
    minimum degree  m  ←  0;
    while there is still  u  s.t.  u  ∈  G  do{
        for all vertexes  u  do{
            if  degree(u)  ≤  m then{
                find direct predessesor  v  of  u;
                A(v)  ←  A(v)  +  e^(-β(T(u)−T(v)))A(u);
                remove  v  from  G;
            }
        }
    }
    return  A(v)  for all  v  in  G, sortbykey(V, sortkey  =  A(v);
```

### Dataset
The Soft-KShell algorithm is compared along with four other algorithms on six real-world data sets with various social interactions, the specifications of the data sets utilized in the studies are listed in Table below.

| Datasets      |  $\|V\|$         | $\|E\|$          | Max degree | Description                                    |
|---------------|------------------|------------------|------------|------------------------------------------------|
|NCF(reply)     | 998              | 541              | 8          |The reply data set includes the posts  (nodes) that are replying  to other posts or being replied to by other posts. The responding relation is represented by a directed edge.|
|NCF(quote)     | 3746             | 2716             | 220        |The quote data set contains posts (nodes) that are quoting other posts or being quoted by other posts.  One quoting interaction is a directed edge.|
|NCF(retweet)   | 35601            | 30251            | 576        |The retweet data set includes posts (nodes) that are either  retweeting other tweets or are being retweeted by other tweets. One retweet interaction is a directed edge.|
|NCF(together)  | 38773            | 33490            | 799        |The network includes a collection of long-term tweets covering the three above interactions (reply, retweet, quote) together.|
|NCJ            | 6242             | 4589             | 161        |The network includes a collection of short-term tweets only consider the replying connections.|
|DBLP V1        | 348480           | 745252           | 1828       |Open citation network extracted from DBLP, ACM, MAG, and other sources.|

where $\|V\|$ denotes the number of vertexes (nodes) in a graph and $\|E\|$ represents the number of edges in a graph.

### Features

* high detection power for large-scale social media datasets
* providing SIR simualtion API within the dataloader class
* Proposed and implemented Soft Secomposition algorithm
* Some other opinion leader mining algorithms including [Leader Rank](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0021202), [K-Shell Iteration Factor](https://www.sciencedirect.com/science/article/abs/pii/S0378437116302333), [Random Influential Path selection](https://arxiv.org/abs/2112.02927), [Mixed degree decomposition](https://www.sciencedirect.com/science/article/abs/pii/S0375960113002260).

### Required python packages

* python == 3.8
* EoN == 1.1
* networkx >= 2.0
* numpy >= 1.13
* pandas

### Optional packages depending on used functions

* matlibplot
* tqdm (Mozilla Public Licence)

