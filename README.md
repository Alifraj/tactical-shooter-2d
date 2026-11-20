# 🎮 Tactical Shooter 2D

Un jeu de tir tactique en **2D** développé avec **Python** et **Pygame** dans le cadre du module de programmation de **1ère Année Ingénieur Informatique**.

---

# 📝 Description

**Tactical Shooter 2D** est un jeu d’action dynamique où le joueur incarne un agent chargé de survivre face à des vagues d’ennemis de plus en plus rapides et agressifs.

Le projet met en pratique plusieurs concepts importants :

* Programmation Orientée Objet (**POO**)
* Gestion des sprites avec **Pygame**
* Détection de collisions
* Gestion des sons et de la musique
* Sauvegarde locale des scores
* Architecture modulaire et propre

---

# 🚀 Fonctionnalités

✅ Système de score et sauvegarde du meilleur score
✅ Difficulté progressive (ennemis plus rapides)
✅ Menu principal interactif
✅ Écran de pause (`P`)
✅ Écran de Game Over
✅ Musique d’ambiance et effets sonores
✅ Gestion optimisée des sprites avec `pygame.sprite.Group`
✅ Architecture orientée objet claire et maintenable

---

# 🛠️ Technologies Utilisées

* **Python 3**
* **Pygame**

---

# 📦 Installation

## 1️⃣ Cloner le projet

```bash
git clone https://github.com/votre-utilisateur/tactical-shooter-2d.git
cd tactical-shooter-2d
```

---

## 2️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Lancer le jeu

```bash
python main.py
```

---

# 🎮 Contrôles

| Action      | Touche              |
| ----------- | ------------------- |
| Déplacement | `ZQSD` ou `Flèches` |
| Tir         | `Espace`            |
| Pause       | `P`                 |
| Quitter     | `ESC`               |

---

# 📂 Structure du Projet

```plaintext
.
├── assets/
│   ├── images/              # Sprites et images du jeu
│   └── sounds/              # Musiques et effets sonores
│
├── main.py                  # Point d’entrée du programme
├── game.py                  # Boucle principale du jeu
├── player.py                # Classe Joueur et projectiles
├── enemy.py                 # Classe Ennemi et logique IA
├── settings.py              # Constantes et configuration
├── highscore.txt            # Sauvegarde du meilleur score
└── requirements.txt         # Dépendances Python
```

---

# 🧠 Concepts Utilisés

* Programmation Orientée Objet (POO)
* Gestion des événements clavier
* Boucle de jeu temps réel
* Détection de collisions
* Gestion audio avec Pygame Mixer
* Sauvegarde de données locales

---

# 📸 Aperçu du Jeu

Ajoutez ici des captures d’écran du jeu :

```md
![Gameplay](assets/images/screenshot.png)
```

---

# 🔮 Améliorations Futures

* Ajout de plusieurs armes
* Système de vies
* Boss de fin de niveau
* Mode multijoueur
* Animations avancées
* Système de niveaux

---

# 👨‍💻 Auteur
Ali Frej

Étudiant en Génie Informatique — École Polytechnique de Sousse

GitHub : @Alifraj
---

# 📜 Licence

Ce projet est réalisé dans un cadre éducatif et académique.
