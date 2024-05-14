---
title: Image generator
author: 
  - Arsène DEGHELA
  - Maxime Jores SIGNE FOKOUI
  - Joel Patrick MOUKOKO
date: 2024-05-14
geometry:
  - top=20mm
  - left=20mm
  - right=10mm
  - bottom=10mm
  - heightrounded
bibliography: [biblio.bib]
---

## Test

``` python
import tensorflow as tf

```

![Alt](media/trucmuch.png)

## Sujet

On souhaite créer un programme qui est capable de génerer une variation d'une image. On lui fournis une image d'origine, un prompt de modification et l'IA fournis un prompt de sortie et l'image associée.

Le but est la modification de style, la recontextualisation de personnages et d'objet.

On est limité par les coûts à l'utilisation, et on peut uniquement utiliser Azure et OpenAI (avec parcimonie).


## État de l'Art

### 1. Modèles de Transformation d'Images

- **GANs (Generative Adversarial Networks)** : Des modèles tels que StyleGAN, CycleGAN, et BigGAN sont souvent utilisés pour la génération d'images stylisées et la modification de contenu. CycleGAN, par exemple, est particulièrement adapté pour la traduction d'images entre deux domaines (par exemple, des photos en peintures).
- **VQ-VAE-2 (Vector Quantized Variational AutoEncoders)** : Utilisé pour la génération de haute qualité, ce modèle apprend des représentations discrètes et peut générer des variations détaillées d'images.
- **DALL-E** : Développé par OpenAI, ce modèle est capable de générer des images à partir de descriptions textuelles et peut être utilisé pour recontextualiser des objets ou personnages dans une image.

### 2. Transformers et Vision Models

- **CLIP (Contrastive Language-Image Pre-Training)** : Combine des images et du texte, permettant de créer des systèmes qui comprennent et génèrent des images basées sur des descriptions textuelles.
- **Vision Transformers (ViT)** : Ces modèles appliquent le concept des transformers, initialement utilisé pour le traitement du langage naturel, à la vision par ordinateur.

### 3. Plateformes et Services Cloud

- **Azure Cognitive Services** : Offre des outils pour la vision par ordinateur, comme Custom Vision et Face API, qui peuvent être intégrés pour des tâches spécifiques de modification d'image.
- **OpenAI API** : Fournit des modèles pré-entraînés comme GPT-4 et DALL-E, qui peuvent être utilisés pour générer des prompts de sortie et des images associées.

## Architechture

### 1. Pipeline de Traitement des Prompts et des Images

#### Input Layer
- **Image d'origine** : Image fournie par l'utilisateur.
- **Prompt de modification** : Description textuelle des modifications souhaitées.

#### Prétraitement
- **Analyse du prompt** : Utilisation de GPT-4 pour analyser et structurer le prompt de modification. Le prompt est divisé en sous-tâches claires (ex. changer le style, ajouter un objet, modifier l'arrière-plan).
- **Extraction de caractéristiques** : Utilisation de CLIP pour comprendre la relation entre le texte et l'image, et pour guider les modifications nécessaires.

#### Modifications Basées sur le Style et le Contexte
- **Style Transfer** : Utilisation de modèles de transfert de style basés sur GANs ou VQ-VAE-2 pour modifier le style de l'image.
- **Recontextualisation des Objets** : Utilisation de DALL-E pour générer des variantes d'objets ou de personnages en fonction du prompt, et les intégrer dans l'image d'origine.

#### Post-Processing
- **Réassemblage** : Combinaison des différents éléments générés (arrière-plan, objets, personnages) pour former l'image finale.
- **Ajustements Finaux** : Utilisation de techniques de filtrage et d'ajustement pour garantir la cohérence visuelle et esthétique de l'image finale.

#### Output Layer
- **Prompt de sortie** : Généré par GPT-4, ce prompt décrit les modifications apportées.
- **Image modifiée** : Image finale résultant des modifications.

### 2. Infrastructure Technique

- **Azure Storage** : Pour stocker les images d'origine et les images générées.
- **Azure Compute Instances** : Pour exécuter les modèles d'IA et les pipelines de traitement.
- **OpenAI API** : Pour accéder aux modèles GPT-4 et DALL-E.
- **Azure Functions** : Pour orchestrer les différentes étapes du pipeline et gérer les appels API.

## Schéma de l'Architecture

```plaintext
+---------------------------+
|        Utilisateur        |
+------------+--------------+
             |
+------------v--------------+
|   Interface Utilisateur   |
+------------+--------------+
             |
+------------v--------------+            +-------------------+
|   Azure Functions (Orchestration)      | OpenAI GPT-4       |
|   - Traitement des Prompts            | - Analyse du prompt|
|   - Appels API                        | - Génération prompt|
+------------+--------------+            +--------^----------+
             |                                |
+------------v--------------+        +--------+----------+
|   Prétraitement & Analyse |        |  OpenAI DALL-E    |
|   - CLIP                  |        |  - Génération d'images |
|   - Extraction de Caractéristiques |        +--------+----------+
+------------+--------------+                 |
             |                                |
+------------v--------------+                 |
|   Modification d'Images   |                 |
|   - GANs / VQ-VAE-2       |                 |
|   - Transfer de Style     |                 |
+------------+--------------+                 |
             |                                |
+------------v--------------+                 |
|    Post-Processing        |                 |
|   - Réassemblage          |                 |
|   - Ajustements Finaux    |                 |
+------------+--------------+                 |
             |                                |
+------------v--------------+                 |
|   Stockage Azure          |                 |
|   - Images d'Origine      |                 |
|   - Images Générées       |                 |
+---------------------------+                 |
             |                                |
+------------v--------------+                 |
|   Interface Utilisateur   |<----------------+
|   - Affichage Résultats   |
+---------------------------+

## etc

## Bibliographie