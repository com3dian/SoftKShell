# Influential Node Detection on Graph on Event Sequence
This repository contains the implementation of the Soft-Kshell algorithm and supplementary results from its application to real-world datasets.

| Data sets     | $|V|$            | $|E|$            | Max degree | Description                                    |
|---------------|------------------|------------------|------------|------------------------------------------------|
|NCF(reply)     | 998              | 541              | 8          |The reply data set includes the posts  (nodes) that are replying  to other posts or being replied to by other posts. The responding relation is represented by a directed edge.|

\hline
 NCF(quote) & 3746 & 2716 & 220 & \makecell{
 The quote data set contains posts (nodes) \\ 
 that are quoting other posts or being quoted \\ 
 by other posts.  One quoting interaction \\ 
 is a directed edge. }\\ 
\hline
 NCF(retweet) & 35601 & 30251 & 576 & \makecell{
 The retweet data set includes posts (nodes) \\ 
 that are either  retweeting other tweets or \\
 are being retweeted by other tweets. One \\ 
 retweet interaction is a directed edge. }\\ 
\hline
 NCF(together) & 38773 & 33490 & 799 & \makecell{
 The network includes a collection of \\
 long-term tweets covering the three above \\
 interactions (reply, retweet, quote) together.}\\
\hline
 NCJ & 6242 & 4589 & 161 & \makecell{
 The network includes a collection of \\ 
 short-term tweets only consider the \\
 replying connections.}\\
\hline
 DBLP V1 & 348480 & 745252 & 1828 & \makecell{
 Open citation network extracted from\\ 
 DBLP, ACM, MAG, and other sources.}\\
 \hline
 \end{tabular}
 \caption{Six real-world data sets with various social interactions.}
 \label{tab: data}
 \end{center}
\end{table*}
