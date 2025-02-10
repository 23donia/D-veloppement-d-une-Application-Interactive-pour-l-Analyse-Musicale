import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Charger le dataset local avec le fichier téléchargé
data = pd.read_csv('songs_normalize.csv')

# Fonction pour la page d'accueil
def home_page():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #E6F7FF;
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1, .welcome-text {
            color: #003366;
            font-size: 40px;
            font-weight: bold;
        }
        .intro-text {
            font-size: 20px;
            color: #004080;
            margin-top: 15px;
        }
        .button {
            background-color: #004080;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .button:hover {
            background-color: #0059b3;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown('''
        <div class="main">
            <div class="welcome-text">Bienvenue sur MusicAnalyzer 🎵</div>
            <p class="intro-text">Découvrez comment les différentes caractéristiques musicales influencent la popularité des chansons et aident les entreprises à maximiser leurs ventes.</p>
            <button class="button" onclick="window.location.href='?page=Tableau%20de%20bord'">Accéder au Dashboard</button>
        </div>
    ''', unsafe_allow_html=True)

# Fonction pour le tableau de bord
def dashboard_page():
    st.title("Tableau de bord interactif")
    st.write("Explorez les données à l'aide de visualisations interactives.")

    st.subheader("Popularité des genres musicaux")
    genre_popularity = data.groupby('genre')['popularity'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(genre_popularity, x='genre', y='popularity', title='Popularité moyenne par genre', color_discrete_sequence=['#003366'])
    st.plotly_chart(fig)

    st.subheader("Dansabilité par genre")
    danceability_genre = data.groupby('genre')['danceability'].mean().sort_values(ascending=False).reset_index()
    fig = px.bar(danceability_genre, x='genre', y='danceability', title='Dansabilité moyenne par genre', color_discrete_sequence=['#003366'])
    st.plotly_chart(fig)

    # Matrice de corrélation
    st.subheader("Matrice de Corrélation")
    corr = data.select_dtypes(include=['int64', 'float64']).corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
    st.pyplot(fig)
    st.write("**Interprétation :** Cette matrice met en évidence les corrélations entre les différentes caractéristiques des chansons. Des corrélations fortes peuvent indiquer des relations significatives à explorer davantage.")

    # Scatter plot des variables les plus corrélées
    st.subheader("Corrélations fortes entre variables")
    strong_corr = corr.abs().unstack().sort_values(ascending=False)
    strong_corr = strong_corr[(strong_corr < 1) & (strong_corr > 0.5)].drop_duplicates()

    for (var1, var2) in strong_corr.index:
        fig = px.scatter(data, x=var1, y=var2, title=f'Corrélation entre {var1} et {var2}', color_discrete_sequence=['#003366'])
        st.plotly_chart(fig)

    # Boxplots interactifs
    st.subheader("Boxplots interactifs")
    numeric_features = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    selected_feature = st.selectbox("Sélectionnez une variable pour voir son boxplot", numeric_features)
    fig = px.box(data, y=selected_feature, title=f'Boxplot de {selected_feature}', color_discrete_sequence=['#003366'])
    st.plotly_chart(fig)

    # Popularité maximale par artiste (sélection de l'artiste)
    st.subheader("Année de la Popularité Maximale par Artiste")
    selected_artist = st.selectbox("Sélectionnez un artiste", data['artist'].unique())
    artist_data = data[data['artist'] == selected_artist]
    max_popularity_year = artist_data.loc[artist_data['popularity'].idxmax()]['year']
    fig = px.bar(artist_data, x='year', y='popularity', title=f'Popularité maximale de {selected_artist}', color_discrete_sequence=['#003366'])
    st.plotly_chart(fig)
    st.write(f"**Interprétation :** L'année de popularité maximale de {selected_artist} est {max_popularity_year}.")

# Application principale
def main():
    page = st.sidebar.selectbox("Navigation", ["Accueil", "Tableau de bord"])

    if page == "Accueil":
        home_page()
    elif page == "Tableau de bord":
        dashboard_page()

if __name__ == "__main__":
    main()
