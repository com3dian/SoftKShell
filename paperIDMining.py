# paperID mining
from dataloader import readData

def findAllNodeByPaperID(dataPath):
    '''
    find node by paperID
    ------------
    dataPath: path of dataset
    '''
    ans = dict()
    
    # the path and sheet name should changed if using different dataset
    dfDict = readData(dataPath, ['with paperID'])
    dfWithPaperID = dfDict['with paperID']
    
    paperIDList = np.array(dfWithPaperID['altmetric_id'].to_list())
    paperIDs = set(paperIDList[np.logical_not(np.isnan(paperIDList))])
    # get papaerID set
    
    for paperID in paperIDs:
        dfID = dfWithPaperID[(dfWithPaperID['altmetric_id'] == paperID)]
        tweets = dfID['tweet_id'].to_list()
        ans[paperID] = tweets
    
    return ans

def plotByPaperID(paperIDs, nodeRank, nodeDictByPaperID):
    '''
    plot a core plot(by using polar coordinates)
    the nodes that are closer to the core are more influential
    nodes mentioned same paperID is color in the same way
    --------------------
    paperID: paper ID
    nodeRank: 
    topNumber: top Nodes number
    '''
    # plt settings
    plt.figure(dpi = 850)
    plt.style.use('ggplot')
    ax = plt.gca(projection='polar')
    ax.set_rlabel_position(0.0)  
    ax.set_rlim(0.0, 1.0)

    # color palette
    colors = ['#f5ed51', 
              '#344CB7',
              '#EA5C2B',
              '#FF6464',
              '#E60965'
             ]
    nodeAngle, nodeR = [], []
    for node in nodeRank.keys():
        nodeR.append(np.exp(- nodeRank[node] + 0.95))
        nodeAngle.append(random.uniform(0, 360))
    plt.scatter(nodeAngle, nodeR,  c = 'grey', s=.5)
    
    i = 0
    for paperID in paperIDs:
        nodePaperAngle, nodePaperR, size = [], [], []
        for node in nodeDictByPaperID[paperID]:
            if node in nodeRank.keys():
                nodePaperR.append(np.exp(- nodeRank[node] + 0.95))
                nodePaperAngle.append(random.uniform(0, 360))
                size.append((1.05 - nodePaperR[-1]) * 10)
                
        plt.scatter(nodePaperAngle, nodePaperR,c = colors[i] , s=size, label = paperID)
        i += 1
    # plotting
    plt.legend(loc=(0.9, 0), fontsize = 6)
    plt.show()
    return 0
