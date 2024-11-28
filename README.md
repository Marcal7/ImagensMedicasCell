# 🧪 Projeto de Processamento de Imagens Médicas 🖼️  

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)  
**Automatizando a análise de biomarcadores em cortes histológicos.**  

---

## 📋 **Resumo**  
Este projeto propõe uma solução automatizada para substituir a análise manual da proteína **PIMREG** em cortes histológicos, utilizando Python e técnicas de processamento de imagens. O software identifica e conta os biomarcadores de interesse com alta eficiência, utilizando bibliotecas como **OpenCV**, **NumPy**, **Pandas** e **Tkinter**.  

### 🚀 **Resultados:**
- **Taxa de acertos:**  
  - 🟦 Núcleos azuis: **70,59%**  
  - 🟫 Núcleos marrons: **35,30%**  

---

## 🎯 **Objetivo**  
Reduzir a intervenção manual e aumentar a precisão na análise de lâminas digitalizadas com a identificação automática dos biomarcadores PIMREG.  

---

## 🛠️ **Funcionalidades**  
### 🔍 **Processamento de imagens**  
- Conversão, pré-processamento e análise automática.  
- Identificação de biomarcadores com **método Otsu** e detecção de contornos.  

### 📊 **Geração de dados**  
- Exportação dos resultados em formato **Excel** com estatísticas detalhadas.  

### 💻 **Interface intuitiva**  
- Desenvolvida em **Tkinter**, com suporte para:  
  - Seleção de diretórios e arquivos.  
  - Visualização do progresso.  
  - Opções para salvar imagens processadas.  

---

## 🗂️ **Estrutura do Projeto**  

### **Frontend:**  
Interface gráfica desenvolvida com **Tkinter**, permitindo interações simples para usuários:  
- Configuração dos diretórios.  
- Início do processamento.  
- Exportação dos resultados.  

### **Backend:**  
Lógica implementada com:  
- **OpenCV:** Manipulação e análise de imagens.  
- **NumPy:** Operações matemáticas e arrays.  
- **Pandas:** Organização e exportação de dados.  

---

## 📖 **Guia de Uso**  

1. **Execute o programa:** Abra o arquivo executável.  
2. **Configuração inicial:**  
   - Selecione a pasta contendo as imagens 📂.  
   - Escolha o diretório de exportação para o arquivo Excel 📊.  
   - Defina o nome do arquivo de saída ✍️.  
3. **Processamento:** Clique em `Iniciar Processamento` e acompanhe a barra de progresso 📈.  
4. **Resultados:**  
   - Imagens processadas salvas (opcional).  
   - Planilha Excel gerada com os dados de contagem.  

---

## ⚙️ **Ferramentas e Bibliotecas**  
- 🟦 **OpenCV:** Processamento de imagens.  
- 📊 **Pandas:** Manipulação de dados e exportação.  
- 🔢 **NumPy:** Operações matemáticas.  
- 🖥️ **Tkinter:** Interface gráfica.  

---

## 💡 **Principais Dificuldades**  
1. **Heterogeneidade nas imagens:** Variação de cores e formatos.  
2. **Fragmentação de núcleos:** Contornos sobrepostos e núcleos irregulares.  
3. **Referência limitada:** Necessidade de confiar nos dados semiautomáticos do ImageJ para validação.  

---

## 📊 **Resultados Obtidos**  
O software é eficiente e rápido, processando imagens em média em **2:49 minutos** por conjunto.  

---

## 📚 **Referências**  
- [OpenCV](https://docs.opencv.org/4.x/index.html)  
- [NumPy](https://numpy.org/doc/stable/)  
- [Pandas](https://pandas.pydata.org/docs/)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html)  

---  

> 💻 Desenvolvido por **Grupo 2** — Faculdade de Medicina de Ribeirão Preto - USP.  
