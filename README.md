# summer_weather

Esse repositório contém os dados, análises e predições do conjunto de dados identificado como "Bias correction of numerical prediction model temperature forecast Data Set", que pode ser encontrado no link: https://archive.ics.uci.edu/ml/datasets/Bias+correction+of+numerical+prediction+model+temperature+forecast.

No desenvolvimento desse projeto também foi considerado o artigo científico que originou esse conjunto de dados, que pode ser encontrado no link: https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019EA000740

Para a completa reprodução dos resultados gerados por esse projeto recomenda-se a instalação das bibliotecas que constam no arquivo "./requirements".

O projeto é composto por dois arquivos do tipo jupyter notebook, que estão na pasta "./notebooks/". O primeiro denominado "exploratory_data_analysis.ipynb" contém uma análise exploratória dos dados, com a geração de um arquivo Pandas Profiling embutido ao final e diversos comentários sobre a composição dos dados. O segundo se chama "modelling.ipynb" e possui todo processo de modelagem e aferição de desempenho, centrado na utilização da biblioteca "pycaret". Ambos os notebooks estão com os outputs de suas células preservados, para facilitar a interpretação dos resultados. Contudo, caso seja o objetivo do leitor, eles podem ser executados novamente.