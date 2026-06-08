# ⚽ Football Squad Rating System

A Python-based football squad management and player rating tool featuring real international squads with detailed player attributes.

## Overview

This project models international football squads with individual player stats, allowing you to select a team and view player ratings in a formatted display. Currently includes full squads for **England** and **Brazil**.

## Features

- Structured `Player` class with detailed attributes
- Full 26-player squads for England and Brazil
- Formatted player rating table output
- Team selection via user input
- Players categorised by position: GK, DF, MF, FW

## Player Attributes

| Attribute  | Description                          |
|------------|--------------------------------------|
| `name`     | Player's full name                   |
| `age`      | Current age                          |
| `shoot`    | Shooting ability (0–100)             |
| `speed`    | Speed/pace (0–100)                   |
| `stamina`  | Stamina/endurance (0–100)            |
| `passing`  | Passing accuracy (0–100)             |
| `tackle`   | Tackling ability (0–100)             |
| `position` | Position (GK, DF, MF, FW)           |
| `ovl`      | Overall rating (0–100)               |

## Getting Started

### Prerequisites

- Python 3.x

### Running the Program

```bash
python main.py
```

You will be prompted to enter a team name:

```
Enter the team you want to play as: England
```

### Example Output

```
==================================================
                PLAYER RATING SYSTEM              
==================================================
Name                 | Age | Pos | Calculated OVL
--------------------------------------------------
Jordan Pickford      | 32  | GK  |      83       
John Stones          | 32  | DF  |      85       
Jude Bellingham      | 22  | MF  |      90       
Harry Kane           | 32  | FW  |      90       
==================================================
```

## Squads Included

### 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England
- **GK:** Pickford, Henderson, Trafford
- **DF:** Stones, Guéhi, Konsa, James, Burn, Livramento, O'Reilly, Quansah, Spence
- **MF:** Bellingham, Rice, Mainoo, Rogers, Anderson, Eze, Henderson J.
- **FW:** Kane, Saka, Rashford, Gordon, Madueke, Toney, Watkins

### 🇧🇷 Brazil
- **GK:** Alisson, Ederson, Weverton
- **DF:** Marquinhos, Gabriel M., Danilo, Bremer, Alex Sandro, Ibañez, Douglas Santos, Léo Pereira
- **MF:** Casemiro, Bruno Guimarães, Paquetá, Fabinho, Éderson (Atalanta), Danilo S.
- **FW:** Vinícius Jr., Neymar, Raphinha, Endrick, Martinelli, Cunha, Luiz Henrique, Igor Thiago, Rayan

## Project Structure

```
├── main.py       # Main script with Player class and squad data
└── README.md     # Project documentation
```

## Planned Features

- [ ] Team selection logic to filter and display chosen squad
- [ ] Best XI auto-selector based on OVL ratings
- [ ] Head-to-head team comparison
- [ ] More international squads (France, Germany, Argentina, etc.)
- [ ] Match simulation engine
