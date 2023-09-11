# Influential Node Detection on Graph on Event Sequence
This repository contains the implementation of the Soft-Kshell algorithm and supplementary information \& results from its application to real-world datasets.

### Algorithm pseudocode
```{r, highlight=TRUE}
# Soft K-shell Algorithm
Data: graph G = (V, E), parameter β, node property α(v), use-node-property
Result: A(v), the overall influence for each vertexes v
 initialization\;
 For all nodes v do{
    if use-node-property is True then{
        A(v) ← α(v);
    }{
        A(v) ← 1;
    }
 }
 minimum degree m ← 0;
 while there is still u s.t. u ∈ G do{
    for all vertexes u do{
        if degree(u) ≤ m then{
            find direct predessesor v of u;
            A(v) ← A(v) + e^(β(T (u)−T (v)))A(u);
            remove v from G;
        }
    }
 }
 return A(v) for all v in G, sortbykey(V, sortkey = A(v);
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
