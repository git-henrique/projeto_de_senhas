# - Cofre de Senhas (Password Vault)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-lightgrey)
![UI](https://img.shields.io/badge/interface-Tkinter-orange)

Meu amigo queria zerar o celular e não queria ter que ficar salvando manualmente as senhas dos seus logins que estavam fora do google em um .txt. Eu avisei que era só botar no gerenciador de senhas da Apple mas ele falou: _"e se tivesse um sistema pra guardar no meu pc?"_ e me lançou a ideia. 
Como eu também não penso muito achei que seria interessante, e então saiu um aplicativo simples de cofre de senhas com interface gráfica desenvolvido em Python.
Permite armazenar, visualizar e atualizar credenciais de forma local no computador.

---

## 🚀 Funcionalidades

* 🔑 Login com senha mestre
* ➕ Adicionar novas credenciais (site, usuário e senha)
* 👁️ Visualizar credenciais armazenadas
* 🔄 Atualizar senha de um site existente
* 💾 Persistência dos dados em arquivo local
* 🔐 Codificação básica das senhas

---

## 🖥️ Interface

O sistema utiliza uma interface gráfica simples com Tkinter, permitindo interação fácil com os dados.

---

## 🛠️ Tecnologias utilizadas

* Python 3
* Tkinter (interface gráfica)
* JSON (armazenamento de dados)
* Base64 (codificação simples)

---

## 📦 Estrutura do projeto

```
├── cofre.py              # Código principal da aplicação
├── cofre.example.dat     # Exemplo de estrutura do cofre
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Documentação do projeto
```

---

## ⚙️ Como executar o projeto

### 1️⃣ Pré-requisitos

* Python 3 instalado

Verifique com:

```
python --version
```

---

### 2️⃣ Executar o projeto

No terminal, dentro da pasta do projeto:

```
python cofre.py
```

---

## 🔐 Sobre o armazenamento das senhas

As senhas são armazenadas em um arquivo local chamado:

```
cofre.dat
```

Esse arquivo:

* é criado automaticamente na primeira execução
* contém os dados codificados
* está listado no `.gitignore` para **não ser enviado ao GitHub**

---

## ⚠️ Aviso de segurança

Este projeto utiliza **Base64**, que é apenas uma forma de codificação, não criptografia segura.

👉 Portanto:

* NÃO utilize este sistema para armazenar senhas reais importantes
* Este projeto é voltado para fins educacionais

---

## 💡 Melhorias futuras

* 🔐 Implementar criptografia forte (AES)
* 🎨 Melhorar interface gráfica
* 🔎 Adicionar busca de credenciais
* 🗑️ Permitir remoção de registros
* 🔑 Hash seguro da senha mestre

---

## 👨‍💻 Autor

Projeto desenvolvido para aprendizado de conceitos como:

* manipulação de arquivos
* interfaces gráficas
* organização de código
* boas práticas com Git

---

## 📄 Licença

Este projeto é livre para uso e modificação para fins educacionais.
