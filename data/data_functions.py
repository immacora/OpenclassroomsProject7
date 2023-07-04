from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).parent
DATASET_0 = BASE_DIR.joinpath('dataset0_Python+P7.csv')
DATASET_1 = BASE_DIR.joinpath('dataset1_Python+P7.csv')
DATASET_2 = BASE_DIR.joinpath('dataset2_Python+P7.csv')

DATAFRAME_0 = pd.read_csv(DATASET_0)
DATAFRAME_1 = pd.read_csv(DATASET_1)
DATAFRAME_2 = pd.read_csv(DATASET_2)


def create_csv_result(csv_name, df):
    """
    Crée le chemin et le nom de fichier.
    Crée le répertoire parent (result) s'il n'existe pas.
    Exporte le dataframe.
    """
    print(f"\nCréation du fichier {csv_name}.\n")

    try:
        filepath = Path('result/', csv_name + '.csv')
        filepath.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(filepath, index=False)
        print(f"Le fichier {csv_name} a été créé, il est consultable depuis le répertoire result.")

    except Exception as e:
        print(f"\nERREUR: Le fichier n'a pas été créé{str(e)}")


def data_cleaning(df, df_name):
    """
    Crée le rapport d'exploration des données.
    Recherche, exporte en csv et supprime :
        les actions d'un prix aberrant (<= 0€)
        les doublons
    Retourne le dataframe nettoyé des données aberrantes et dupliquées.
    """
    print(f"\nRapport d'exploration des données initiales du {df_name}.")

    df_describe = df.describe()
    print(df_describe)

    df_aberrant_price = df[df.price <= 0]
    csv_name = f"ABERRANT_PRICE_{df_name}"
    create_csv_result(csv_name, df_aberrant_price)
    print(f"\nNettoyage des actions de prix aberrants du fichier {df_name}.")
    indexNames = df[(df['price'] <= 0)].index
    df.drop(indexNames, inplace=True)

    df_duplicated = df.loc[df['name'].duplicated(keep=False), :]
    csv_name = f"DUPLICATED_{df_name}"
    create_csv_result(csv_name, df_duplicated)
    print(f"\nNettoyage des doublons du fichier {df_name}.")
    df.drop_duplicates(subset="name", keep=False, inplace=True)

    return df
