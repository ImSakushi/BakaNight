init:
    $ config.font_replacement_map["InriaSerif-Regular.ttf", False, True] = ("InriaSerif-Italic.ttf", False, False)
    define M = Character("MARCHAND", what_prefix='"', what_suffix='"', color="#a2a2c8")
    define MC = Character("VOUS" , what_prefix='"', what_suffix='"', color="#a2c8a2")
    define OJSP = Character("OUVRIER", what_prefix='"', what_suffix='"', color="#a2a2c8")
    define O = Character("OUVRIER", what_prefix='"', what_suffix='"', color="#a2a2c8")
    define P = Character("PIERRE LACOUR", what_prefix='"', what_suffix='"', color="#a2a2c8")
    define pensees = Character("VOUS", what_prefix="{i}(", what_suffix="){/i}", color="#a2c8a2")

image marchand mr1 = Transform("images/marchand/mr1.png", zoom=1.3)
image marchand mrmouth = Transform("images/marchand/mrmouth.png", zoom=1.3)
image marchand mrpointing = Transform("images/marchand/mrpointing.png", zoom=1.3)
image ouvrier ovr1 = Transform("images/ouvrier/ovr1.png", zoom=1.3)
image ouvrier ovrp = Transform("images/ouvrier/ovrp.png", zoom=1.3)
image ouvrier ovrmouth = Transform("images/ouvrier/ovrmouth.png", zoom=1.3)
image pierre plc1 = Transform("images/pierre/plc1.png", zoom=1.3)
image pierre plcm = Transform("images/pierre/plcm.png", zoom=1.3)
image pierre plcsp = Transform("images/pierre/plcsp.png", zoom=1.3)
image pierre plcf = Transform("images/pierre/plcf.png", zoom=1.3)
image black = Transform("images/black.png", zoom=20, alpha=0.45)
image black2 = Transform("images/black.png", zoom=20, alpha=0.70)

# Pour les images avec transparence 60%
image marchand mr1t = Transform("images/marchand/mr1.png", zoom=1.3, alpha=0.6)
image marchand mrmoutht = Transform("images/marchand/mrmouth.png", zoom=1.3, alpha=0.6)
image ouvrier ovr1t = Transform("images/ouvrier/ovr1.png", zoom=1.3, alpha=0.6)
image ouvrier ovrmoutht = Transform("images/ouvrier/ovrmouth.png", zoom=1.3, alpha=0.6)

image hotel = "images/hotel.jpg"

transform credits_scroll:
    yalign 1.0
    linear 20.0 yalign -1.0

screen credits_screen():
    tag menu  # Utilisez un tag approprié si nécessaire
    text """Histoire interactive par :

    Pablo CASOLA

    Bryan GONCALVES

    Matthias CASA NOVA

    Hugo GITTON

    Titouan GONZALEZ

    Driss CHIARI-NOBLET



    Merci à tous les intervenants
    de MMI Bordeaux pour leur aide.""" align (.5, .0) size 60 at credits_scroll



image empty:
    "images/empty_1.png"
    pause 0.4
    "images/empty_2.png"
    pause 0.4
    "images/empty_3.png"
    pause 0.4
    "images/empty_4.png"
    pause 0.4
    repeat

init python:
    sexe_choisi = ""
    confirmed_choice = False


screen choix_sexe:
    zorder 100
    frame:
        background "black"
        align (.5, .5)  # Centre l'élément dans l'écran
        vbox:
            text "Choisissez votre genre :" align (.5, .5) size 50
            spacing 20  # Augmente l'espace entre les éléments pour une meilleure lisibilité
            textbutton "Homme" action [SetVariable("sexe_choisi", "Homme"), Hide("choix_sexe"), Jump("dialogues_personnage")] align (.5, .5) text_size 50
            textbutton "Femme" action [SetVariable("sexe_choisi", "Femme"), Hide("choix_sexe"), Jump("dialogues_personnage")] align (.5, .5) text_size 50
            textbutton "Non-binaire" action [SetVariable("sexe_choisi", "Non-binaire"), Hide("choix_sexe"), Jump("dialogues_personnage")] align (.5, .5) text_size 50

# label main_menu:
#     "Cliquez pour commencer"
#     $ renpy.pause()  # Cette pause attend une interaction utilisateur
#     jump start

label start:
    scene empty
    call choix_personnage

label choix_personnage:
    window hide
    $ confirmed_choice = False
    while not confirmed_choice:
        show screen choix_sexe
        $ renpy.pause()  # Cette pause attend une interaction utilisateur

label dialogues_personnage:
    pensees "Où suis-je ?"
    pensees "J’étais au Musée il y a même pas une minute."
    if sexe_choisi == "Homme":
        pensees "Est-ce que j'ai été absorbé par le tableau ?!"
    elif sexe_choisi == "Femme":
        pensees "Est-ce que j'ai été absorbée par le tableau ?!"
    else:
        pensees "Est-ce que j'ai été absorbé.e par le tableau ?!"
    pensees "Comment est-ce possibl-{nw}"
    scene bg_1 with fade
    $ renpy.block_rollback()
    show marchand mrmouth zorder 2 at tcommon(500)
    if sexe_choisi == "Homme":
        M "Vous allez bien, monsieur ?"
    elif sexe_choisi == "Femme":
        M "Vous allez bien, madame ?"
    else:
        M "Vous allez bien ?"
    show marchand mr1
    if sexe_choisi == "Homme":
        M "Vous semblez tout pâle."
    elif sexe_choisi == "Femme":
        M "Vous semblez toute pâle."
    else:
        M "Vous semblez tout.e pâle."

    menu:
        "Qui êtes-vous ?":
            jump qui_etes_vous

        "Où sommes-nous ?":
            jump ou_sommes_nous

label qui_etes_vous:
    MC "Qui êtes-vous ?"
    show marchand mrmouth
    M "Je ne suis qu’un humble marchand."
    M "Je reviens tout juste d’un périple en Chine."
    M "J’y ai goûté le plus savoureux des thés !"
    MC "Et où allons-nous ?"
    show marchand mrpointing at tcommon(450)
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    show marchand mr1 at tcommon(500)
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    show black zorder 3
    pensees "J’étais déjà à Bordeaux, qu’est-ce qu’il se passe ?"
    hide black
    jump dialogue_apres_choix

label ou_sommes_nous:
    MC "Où sommes-nous ?"
    show marchand mrmouth
    M "À bord du navire marchand le plus éminent d’Europe !"
    M "Je reviens tout juste d’un voyage en Chine."
    M "J’y ai goûté le plus savoureux des thés !"
    MC "Et où allons-nous ?"
    show marchand mrpointing at tcommon(450)
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    show marchand mr1 at tcommon(500)
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    show black zorder 3
    pensees "J’étais déjà à Bordeaux,{w=0.3} qu’est-ce qu’il se passe ?"
    hide black
    jump dialogue_apres_choix

label dialogue_apres_choix:
    show marchand mr1
    MC "Vous savez où se trouve le Musée des Beaux Arts ?"
    MC "Je viens de là-bas et j’aimerais y retourner."
    M "Je ne connais pas assez les lieux pour vous aider..."
    show marchand mrmouth
    M "Cependant,{w=0.3} l’homme au haut-de-forme appuyé sur la balustrade saura vous guider."
    M "Il s’appelle Pierre Lacour."
    M "C’est un peintre connu qui connaît la ville comme sa poche."
    hide marchand mrmouth with fade
    pensees "Je ne vois pas comment un peintre pourrait m'aider à retourner à mon époque..."
    pensees "Mais je n’ai aucune autre piste, ça ne coûte rien d’essayer."
    menu:
        "Se diriger vers le peintre":
            jump ouvrier

label ouvrier:
    scene bg_ouvrier with fade
    MC "Je le vois,{w=0.3} ça doit être lui le fameux peintr..."
    show ouvrier ovrmouth zorder 2 at tcommon(500)
    if sexe_choisi == "Homme":
        OJSP "HO LÀ,{w=0.3} MONSIEUR !"
    elif sexe_choisi == "Femme":
        OJSP "HO LÀ,{w=0.3} MADAME !"
    else:
        OJSP "HO LÀ,{w=0.3} VOUS !"
    OJSP "C’est quoi ce bloc de métal que vous tenez la main ?"
    OJSP "D’où est-ce que vous venez ?"
    show black zorder 3
    pensees "Mais,{w=0.3} c’est qui lui ?"
    hide black
    show ouvrier ovrmouth

    menu:
        "Répondre":
            jump repondre

        #"Ne rien dire":
            #jump ne_rien_dire

        "Continuer sa route":
            jump peintre

label repondre:
    show ouvrier ovr1
    MC "C’est mon téléphone."
    show ouvrier ovrmouth
    OJSP "Aucune idée de ce que c’est."
    OJSP "Bref, faites attention à vous il y en a qui travaillent ici."
    show ouvrier ovrp
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    show ouvrier ovr1
    MC "Je vous remercie."
    show ouvrier ovrmouth
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Allez-vous-en avant de salir vos beaux habits."
    hide ouvrier ovr1 with fade
    menu:
        "Aborder le peintre":
          jump peintre

label ne_rien_dire:
    MC "…"
    OJSP "Ici vous ne trouverez que de simples ouvriers acharnés."
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    MC "…"
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Ravi d’avoir parlé avec vous !"
    hide ouvrier ovr1 with fade
    pensees "Parlé ?{w=0.3} Qu’est-ce qu’il raconte ?"
    menu:
        "Aborder le peintre":
          jump peintre

label peintre:
    scene bg_peintre with fade
    MC "Excusez-moi monsieur,{w=0.3} seriez-vous peintre ?"
    show pierre plc1 zorder 2 at tcommon(500)
    P "En effet,{w=0.3} que me voulez-vous ?"
    MC "J’ai besoin de me rendre au Musée des Beaux Arts."
    MC "Sauriez-vous où il se trouve ?"
    show pierre plcsp
    P "Si je sais où il se trouve ?"
    P "Je l’ai fondé,{w=0.3} bien sûr que je le sais."
    show pierre plcm
    P "Malheureusement nous sommes dimanche aujourd’hui et il est fermé."
    P "Je pourrais vous y accompagner demain dès la première heure."
    show pierre plc1
    MC "Je n’ai aucun endroit où loger cette nuit,{w=0.3} je ne peux pas attendre."
    hide pierre plc1 with dissolve
    show hotel zorder 1 with dissolve
    P "Vous voyez l’hôtel derrière moi ?"
    P "C’est l'Hôtel Fenwick,{w=0.3} un somptueux hôtel particulier construit pour le consul des États-Unis Joseph Fenwick."
    show pierre plcm zorder 2 at tcommon(500)
    hide hotel with dissolve
    if sexe_choisi == "Homme":
        P "J’ai été invité à y dormir cette nuit,{w=0.3} un invité de plus ne les dérangerait pas."
    elif sexe_choisi == "Femme":
        P "J’ai été invité à y dormir cette nuit,{w=0.3} une invitée de plus ne les dérangerait pas."
    else:
        P "J’ai été invité à y dormir cette nuit, un.e invité.e de plus ne les dérangerait pas."
    show pierre plc1
    MC "Je vous remercie, mais je n’ai aucun moyen de vous payer."
    show pierre plcf
    P "Eh bien,{w=0.3} permettez-moi de vous proposer ceci,"
    P "Vous avez un profil tout à fait singulier que j'aimerais grandement immortaliser."
    P "Alors,{w=0.3} vous me laissez vous peindre,{w=0.3} et je vous offre la nuitée."
    P "Qu’en dites-vous ?"

    menu:
        "C’est d’accord.":
            jump peinture_accord

        "Euh…":
            jump peinture_hesitation

label peinture_accord:
    show pierre plcm
    P "Parfait !{w=0.3} Pourriez-vous vous placer ici ?"
    P "Je vais vous peindre par-dessus cette esquisse du musée que j’ai commencer hier soir."
    P "Je commence."
    hide pierre plcm with dissolve
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    MC "Je me sens bizarre…"
    scene defor_1
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "Vous dégagez un air vraiment très particulier."
    $ renpy.pause(1)
    MC "Comme si je partais…"
    show black zorder 3
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "J’approche de la fin."
    show black2 zorder 3
    $ renpy.pause(1.5)
    # Attendre un peu
    P "Voilà qui est fait !"
    P "Bon voyage !"
    # Fondu en noir crédit de fin
    jump credit

label peinture_hesitation:
    show pierre plcm
    MC "Euh, je sais pas trop…"
    P "Laissez-moi vous convaincre !"
    P "Voici l'une de mes récentes peintures,{w=0.3} vous m’en direz des nouvelles."
    # Insérer l'image avec un fondu
    show peinture zorder 3 at truecenter with Dissolve(1.0)
    # Attendre un clic de l'utilisateur
    pause
    MC "Il a un certain talent, c’est indéniable."
    MC "Ce n’est peut-être pas une mauvaise idée au final."
    hide peinture with Dissolve(1.0)
    MC "Bon, c’est d’accord."
    jump peinture_accord

label credit:
    scene empty
    show screen credits_screen with fade
    $ renpy.pause(20.0)  # Adaptez la durée selon la longueur de votre défilement et la vitesse souhaitée
    # Vous pouvez ajouter une musique de fond pour les crédits ici
    # $ renpy.music.play("musique_credit.mp3")
    hide screen credits_screen with fade
    # $ renpy.music.stop()  # Arrêter la musique de fond après les crédits si nécessaire
    jump start # Ou toute autre logique pour la suite
