## grafico um com a malha ##
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

plt.style.use('seaborn-muted') ## adiciona cores ##
##print(plt.style.available)

solar = pd.read_csv("MANCHAS.csv") 

plt.plot(solar.Ano, solar.manchas)

plt.xlabel('ANO (s)')

plt.ylabel('Mancha')

plt.title('Manchas Solares')

plt.grid(True)

plt.xticks(solar.Ano, solar.Ano)

plt.savefig('grafico1.jpg')

plt.show()

## 10 primeiros com malha##
# com malha#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt 

solar = pd.read_csv("MANCHAS.csv") 

solar1 = solar[0:10]

plt.plot(solar1.Ano, solar1.manchas)

plt.xlabel('ANO (s)')

plt.ylabel('Mancha')

plt.title('Mancha solar 10 primeiros')

plt.grid(True)

plt.xticks(solar1.Ano, solar1.manchas, rotation = 'vertical')

plt.savefig('10primeiros.jpg')

plt.show()

## 10 ultimos com malha##
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

solar = pd.read_csv("MANCHAS.csv") 
solar1 = solar[164:]

plt.plot(solar1.Ano, solar1.manchas)

plt.xlabel('ANO (s)')

plt.ylabel('Quantidade')

plt.title('MANCHAS SOlARES 10 ultimos')

plt.grid(True)

plt.xticks(solar1.Ano, solar1.Ano, rotation = 'vertical')

plt.savefig('10ultimos.jpg')

plt.show()


#gerando box com malha#

import pandas as pd
import matplotlib.pyplot as plt 

solar1 = pd.read_csv("MANCHAS.csv") 

plt.boxplot(solar1.manchas)

plt.xlabel('ANO(s)')

plt.ylabel('Manchas')

plt.title('Quantidade de Manchas Solares')

plt.grid(True)

plt.savefig('box.jpg')

plt.show() 
