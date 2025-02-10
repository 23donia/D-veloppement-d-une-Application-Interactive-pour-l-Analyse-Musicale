# MusicAnalyzer 🎵

## Description de l'application

MusicAnalyzer est une application interactive développée avec Streamlit qui permet d'analyser des données musicales. Elle aide les entreprises de production musicale à identifier les caractéristiques des chansons qui maximisent la popularité et les ventes. L'application offre des visualisations interactives pour explorer des métriques telles que la popularité par genre, la dansabilité, la corrélation entre les attributs audio, et bien plus encore.

## Fonctionnalités principales :
- **Popularité des genres musicaux** : Visualisation des genres les plus populaires.
- **Dansabilité par genre** : Analyse des chansons les plus dansantes par genre.
- **Matrice de corrélation** : Identifier les relations entre les différentes caractéristiques musicales.
- **Scatter Plots des corrélations fortes** : Visualisation des corrélations significatives.
- **Boxplots interactifs** : Explorer la distribution des attributs audio.
- **Analyse de la popularité par artiste** : Identifier l'année de popularité maximale pour chaque artiste.

---

## Aperçu de l'application

### Page d'accueil

<img width="801" alt="image" src="https://github.com/user-attachments/assets/cfdc6bad-d395-4922-937a-30f7161a110f" />


### Tableau de bord interactif

- **Popularité des genres musicaux**

![Popularité des genres musicaux](./path_to_image/file-Jh48nV9zq5Ms8KT3ffkyAx.png)

- **Corrélations fortes entre variables**

![Corrélations fortes entre variables](./path_to_image/file-R6X1UQMbtfgKtrjyERwYFj.png)

---

## Instructions d'installation et d'exécution

1. **Cloner le dépôt GitHub :**
   ```bash
   git clone https://github.com/votre-utilisateur/music-analyzer.git
   cd music-analyzer
   ```

2. **Créer et activer un environnement virtuel (optionnel mais recommandé) :**
   ```bash
   python -m venv env
   source env/bin/activate  # Pour Linux/macOS
   env\Scripts\activate     # Pour Windows
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
   (Si `requirements.txt` n'est pas présent, installez les bibliothèques principales :)
   ```bash
   pip install streamlit pandas plotly seaborn matplotlib
   ```

4. **Exécuter l'application :**
   ```bash
   streamlit run app.py
   ```

5. **Accéder à l'application :**
   Ouvrez votre navigateur et rendez-vous sur [http://localhost:8501](http://localhost:8501).

---

## Choix techniques

- **Langage de programmation :** Python 3.x
- **Framework Web :** [Streamlit](https://streamlit.io/) pour la création de l'interface utilisateur interactive.
- **Visualisation des données :**
  - [Plotly](https://plotly.com/python/) : Graphiques interactifs (barplots, scatter plots, boxplots).
  - [Seaborn](https://seaborn.pydata.org/) et [Matplotlib](https://matplotlib.org/) : Matrice de corrélation et graphiques statistiques.
- **Analyse des données :** [Pandas](https://pandas.pydata.org/) pour la manipulation des données.

---

## Lien vers l'application déployée

Vous pouvez tester l'application directement en ligne via ce [lien](https://your-deployment-link.com).

---












