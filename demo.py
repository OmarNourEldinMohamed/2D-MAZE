from pyMaze import maze, COLOR, agent, textLabel
m = maze(3,10) #default size is 10 x 10 if the brackets are empty
m.CreateMaze(theme=COLOR.dark, loopPercent=100)
#when using load maze the size doesnt matter as it will load the size from the csv file
a = agent(m, footprints=True, filled=True, shape='arrow')
l1 = textLabel(m, 'Total cells', m.rows*m.cols)
#b = agent(m,5, 5, footprints=True, filled=True, color='green')
#path2 = [(5,5), (6,5), (4,5), (2,1), (3,1), (4,1), (6,1), (2,1)]
m.markCells = [(5,5), (6,5), (4,5), (2,1), (3,1), (4,1), (6,1), (2,1)]
#m.tracePath({a:m.path}, delay=100, showMarked=True)

m.run()