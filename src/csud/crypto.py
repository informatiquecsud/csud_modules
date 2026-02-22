import matplotlib.pyplot as plt
from random import shuffle

def permutate_abc(alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    # Convertir l'alphabet en une liste de caractères
    chars = list(alphabet)
    # Mélanger aléatoirement les caractères
    shuffle(chars)
    # Reconstituer une chaîne à partir de la liste mélangée
    permutation = "".join(chars)
    return permutation

def rotate(shift):
    '''
    >>> rotate(3)
    'DEFGHIJKLMNOPQRSTUVWXYZABC'
    >>> rotate(0)
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    >>> rotate(25)
    'ZABCDEFGHIJKLMNOPQRSTUVWXY'
    '''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = ''

    for i in range(len(alphabet)):
        shifted_index = (i + shift) % len(alphabet)
        shifted_alphabet += alphabet[shifted_index]

    return shifted_alphabet


def substitution(text: str, key: str, decrypt: bool = False, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> str:
    '''
    >>> key = 'QOLWNXTMGDKBPRSEUVFZHJIYCA'
    >>> substitution('SALUT', key)
    'FQBHZ'
    >>> substitution('salut', key)
    'FQBHZ'
    >>> substitution('FQBHZ', key, decrypt=True)
    'SALUT'
    '''
    # Initialisation du texte chiffré comme une chaîne vide
    result = ''

    # Pour chaque caractère dans le texte à traiter
    for char in text:
        if char.upper() in alphabet:
            if decrypt:
                index = key.index(char.upper())
                newchar = alphabet[index]
            else:
                index = alphabet.index(char.upper())
                newchar = key[index]
            # Ajout de la lettre chiffrée au texte chiffré en construction
            result += newchar
        else:
            # Si le caractère n'est pas dans l'alphabet, on l'ajoute tel quel au résultat
            result += char

    # Après avoir traité tous les caractères, on retourne le texte chiffré
    return result

def vigenere(text, key, decrypt=False, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    '''
    Chiffre le texte en clair avec le chiffre de Vigenère utilisant la clé donnée.

    >>> vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    >>> vigenere('HELLOCRYPTO', 'KEY')
    'RIJVSABCNDS'
    >>> vigenere("Hello crypto", "KEY")
    'RIJVSMVWZXM'
    >>> vigenere("LXFOPVEFRNHR", "LEMON", decrypt=True)
    'ATTACKATDAWN'
    '''
    ciphertext = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.upper() in alphabet:
            key_index = i % key_length
            abc_index = alphabet.index(char.upper())
            key_char = key[key_index].upper()
            key_shift = alphabet.index(key_char)
            if decrypt:
                key_shift = -key_shift
            shift = (abc_index + key_shift) % len(alphabet)
            encrypted_char = alphabet[shift]
            ciphertext.append(encrypted_char)

    return ''.join(ciphertext)

def letter_frequencies(message: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> list[tuple[str, float]]:
    '''
    Retourne une liste contenant le nombre d'apparitions de chaque
    lettre dans le message

    >>> letter_frequencies("ABCA", "ABC")
    [('A', 50.0), ('B', 25.0), ('C', 25.0)]
    >>> letter_frequencies("HELLO WORLD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    [('A', 0.0), ('B', 0.0), ('C', 0.0), ('D', 9.09), ('E', 9.09), ('F', 0.0), ('G', 0.0), ('H', 9.09), ('I', 0.0), ('J', 0.0), ('K', 0.0), ('L', 27.27), ('M', 0.0), ('N', 0.0), ('O', 18.18), ('P', 0.0), ('Q', 0.0), ('R', 9.09), ('S', 0.0), ('T', 0.0), ('U', 0.0), ('V', 0.0), ('W', 9.09), ('X', 0.0), ('Y', 0.0), ('Z', 0.0)]
    '''
    counters = [0] * len(alphabet)
    # Comptage des lettres
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            counters[index] += 1

    # Calcul des fréquences d'apparition en pourcentage
    frequencies = []
    for i in range(len(alphabet)):
        count = counters[i]
        letter = alphabet[i]
        frequency = round(count / len(message) * 100, 2)  # en pourcentage
        frequencies.append((letter, frequency))

    return frequencies


def plot_frequencies(frequencies: list[tuple[str, float]], title: str, order_by: str = 'frequency', start: int = 0, nbars: int = None) -> None:
    '''
    Affiche un graphique des fréquences d'apparition des lettres
    '''
    def order_by_frequency(x):
        ''' ordre décroissant des fréquences '''
        return -x[1]

    def order_by_letter(x):
        ''' ordre alphabétique des lettres '''
        return ord(x[0])

    nbars = len(frequencies) if nbars is None else nbars

    # Tri selon la méthode choisie
    if order_by == 'frequency':
        frequencies.sort(key=order_by_frequency)
    else:
        frequencies.sort(key=order_by_letter)

    letters = [item[0] for item in frequencies[start:start+nbars]]
    values =  [item[1] for item in frequencies[start:start+nbars]]

    # Créer une figure avec une meilleure résolution
    plt.figure(figsize=(8, 6), dpi=100)

    bars = plt.bar(letters, values)

    # Ajouter les valeurs sur les barres
    for i, (letter, value) in enumerate(zip(letters, values)):
        plt.text(i, value + 0.5, f'{value:.1f}', ha='left', va='bottom', fontsize=8, rotation=45)

    plt.xlabel('Lettres')
    plt.ylabel('Fréquence d\'apparition (%)')
    plt.title(f'Fréquences d\'apparition des lettres dans {title}')
    plt.ylim(0, max(values) + 5)
    plt.show()

french_frequencies = [
    ('A' , 8.15), ('B' , 0.97), ('C' , 3.15), ('D' , 3.73), ('E' , 17.39),
    ('F' , 1.12), ('G' , 0.97), ('H' , 0.85), ('I' , 7.31), ('J' , 0.45),
    ('K' , 0.02), ('L' , 5.69), ('M' , 2.87), ('N' , 7.12), ('O' , 5.28),
    ('P' , 2.80), ('Q' , 1.21), ('R' , 6.64), ('S' , 8.14), ('T' , 7.22),
    ('U' , 6.38), ('V' , 1.64), ('W' , 0.03), ('X' , 0.41), ('Y' , 0.28),
    ('Z' , 0.15),
]

def prepare(text, alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    '''

    Prepares the text to be encrypted by stripping away the
    spaces, punctuation and non latin characters.

    >>> prepare('salut')
    'SALUT'
    >>> prepare("Il m'a toujours impressionné![]{}?")
    'ILMATOUJOURSIMPRESSIONNE'
    '''

    result = ''
    # tout mettre en majuscules
    text = text.lower()
    for c in text:
        if c in alphabet + alphabet.lower():
            c = c
        elif c in 'éèëê':
            c = 'E'
        elif c in 'áàâä':
            c = 'A'
        elif c in 'ûùü':
            c = 'U'
        elif c in 'îïì':
            c = 'I'
        elif c in 'öôò':
            c = 'O'
        elif c in 'ç':
            c = 'C'
        elif c in 'œ':
            c = 'OE'
        else:
            c = ''
        result += c
    return result.upper()


def load_text(filename: str) -> str:
    '''
    Retourne le contenu textuel du fichier `filename`

    Exemple: data = load_text('fichier.txt')
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def friedman_characteristic(text: str, alphabet: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') -> float:
    '''
    Calcule la caractéristique de Friedman pour le texte donné, arrondie à 5 chiffres.

    >>> friedman_characteristic("HELLO")
    0.24154
    >>> friedman_characteristic("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    0.0
    '''
    # Calcul des fréquences des lettres dans le texte
    freqs: list[tuple[str, float]] = letter_frequencies(text, alphabet)
    # Calcul de la caractéristique de Friedman en utilisant la formule
    cf = 0.0
    for i in range(len(alphabet)):
        f_x = freqs[i][1]  # Fréquence de la lettre i
        f_x /= 100  # Convertir en probabilité entre 0 et 1
        cf += (f_x - 1/len(alphabet)) ** 2
    return round(cf, 5)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
