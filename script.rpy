init:
    define M = Character("MARCHAND", what_prefix='"', what_suffix='"', color="#c8a2c8")
    define MC = Character("VOUS" , what_prefix='"', what_suffix='"', color="#a2c8a2")
    define OJSP = Character("???", what_prefix='"', what_suffix='"', color="#c2c8a2")
    define O = Character("OUVRIER", what_prefix='"', what_suffix='"', color="#c2c8a2")
    define P = Character("PEINTRE", what_prefix='"', what_suffix='"', color="#a2a2c8")

image marchand mr1 = "images/marchand/mr1.png"
image marchand mrmouth = "images/marchand/mrmouth.png"
image marchand mrpointing = "images/marchand/mrpointing.png"
image ouvrier ovr1 = "images/ouvrier/ovr1.png"


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
            text "Choisissez votre sexe :" align (.5, .5) size 50
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
    "Où suis-je ?"
    "J’étais au Musée il y a même pas une minute."
    "Comment est-ce possibl-{nw}"
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
    "Comment est-ce que j’ai atterri ici ?"
    MC "Et où allons-nous ?"
    show marchand mrpointing at tcommon(450)
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    show marchand mr1 at tcommon(500)
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    "J’étais déjà à Bordeaux, qu’est-ce qu’il se passe ?"
    jump dialogue_apres_choix

label ou_sommes_nous:
    MC "Où sommes-nous ?"
    show marchand mrmouth
    M "À bord du navire le plus éminent marchand d’Europe !"
    M "Je reviens tout juste d’un voyage en Chine."
    M "J’y ai goûté le plus savoureux des thés !"
    if sexe_choisi == "Homme":
        "Comment est-ce que j’ai atterri ici ?"
    elif sexe_choisi == "Femme":
        "Comment ai-je atterri ici ?"
    else:
        "Mais{w=0.3} qu’est-ce que je fais ici ?"
    MC "Et où allons-nous ?"
    show marchand mrpointing at tcommon(450)
    M "Tout droit vers les quais de Bordeaux !"
    MC "Bordeaux ?"
    M "Bordeaux,{w=0.3} le port de la lune !"
    show marchand mr1 at tcommon(500)
    M "Ce nom vient de la forme en croissant du fleuve,{w=0.3} ça ne vous dit rien ?"
    "J’étais déjà à Bordeaux,{w=0.3} qu’est-ce qu’il se passe ?"
    jump dialogue_apres_choix

label dialogue_apres_choix:
    MC "Vous savez où se trouve le Musée des Beaux Arts ?"
    MC "Je viens de là-bas et j’aimerais y retourner."
    M "Je ne connais pas assez les lieux pour vous aider..."
    show marchand mrmouth
    M "Cependant,{w=0.3} l’homme au haut-de-forme appuyé sur la balustrade saura vous guider."
    M "Il s’appelle Pierre Lacour."
    M "C’est un peintre connu qui connaît la ville comme sa poche."
    M "Il a même fondé un tout nouveau musée,{w=0.4} le musée des Beaux-Arts !"
    "Je ne vois pas comment un peintre pourrait m'aider à retourner à mon époque..."
    "Mais je n’ai aucune autre piste, ça ne coûte rien d’essayer."
    jump ouvrier

label ouvrier:
    scene bg_ouvrier with fade
    MC "Je le vois,{w=0.3} ça doit être lui le fameux peint-{nw}"
    show ouvrier ovr1 zorder 2 at tcommon(500)
    if sexe_choisi == "Homme":
        OJSP "HO LÀ,{w=0.3} MONSIEUR !"
    elif sexe_choisi == "Femme":
        OJSP "HO LÀ,{w=0.3} MADAME !"
    else:
        OJSP "HO LÀ,{w=0.3} VOUS !"
    OJSP "C’est quoi ce bloc de métal que vous tenez la main ?"
    OJSP "D’où est-ce que vous venez ?"
    "Mais,{w=0.3} c’est qui lui ?"

    menu:
        "Répondre":
            jump repondre

        "Ne rien dire":
            jump ne_rien_dire

label repondre:
    MC "C’est mon téléphone."
    OJSP "Aucune idée de ce que c’est."
    OJSP "Bref, faites attention à vous il y en a qui travaillent ici."
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    MC "Je vous remercie."
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Allez-vous-en avant de salir vos beaux habits."
    jump peintre

label ne_rien_dire:
    MC "…"
    OJSP "Ici vous ne trouverez que de simples ouvriers acharnés."
    O "Si c’est la haute société que vous cherchez,{w=0.3} ça se passe là-haut."
    MC "…"
    O "Bon,{w=0.3} c’est pas tout,{w=0.3} mais faut que je retourne travailler moi."
    O "Ravi d’avoir parlé avec vous !"
    "Parlé ?{w=0.3} Qu’est-ce qu’il raconte ?"
    jump peintre

label peintre:
    scene bg_peintre with fade
    MC "Excusez-moi monsieur,{w=0.3} seriez-vous peintre ?"
    P "En effet,{w=0.3} que me voulez-vous ?"
    MC "J’ai besoin de me rendre au Musée des Beaux Arts."
    MC "Sauriez-vous où il se trouve ?"
    P "Si je sais où il se trouve ?"
    P "Je l’ai fondé,{w=0.3} bien sûr que je le sais."
    P "Malheureusement nous sommes dimanche aujourd’hui et il est fermé."
    P "Je pourrais vous y accompagner demain dès la première heure."
    MC "Je n’ai aucun endroit où loger cette nuit,{w=0.3} je ne peux pas attendre."
    P "Vous voyez l’hôtel derrière moi ?"
    P "C’est l'Hôtel Fenwick,{w=0.3} un somptueux hôtel particulier construit pour le consul des États-Unis Joseph Fenwick."
    if sexe_choisi == "Homme":
        P "J’ai été invité à y dormir cette nuit,{w=0.3} un invité de plus ne les dérangerait pas."
    elif sexe_choisi == "Femme":
        P "J’ai été invité à y dormir cette nuit,{w=0.3} une invitée de plus ne les dérangerait pas."
    else:
        P "J’ai été invité à y dormir cette nuit, un.e invité.e de plus ne les dérangerait pas."
    MC "Je vous remercie, mais je n’ai aucun moyen de vous payer."
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
    P "Parfait !{w=0.3} Pourriez-vous vous placez ici ?"
    P "Je vais vous peindre par dessus cette esquisse du musée que j’ai commencé hier soir."
    P "Je commence."
    MC "Je me sens étrange…"
    # Transition ou effet pour montrer le passage du temps
    P "Vous avez un air vraiment très particulier."
    MC "Comme si je partais…"
    # Encore une transition ou effet
    P "J’approche de la fin."
    P "Voilà qui est fait !"
    P "Bon voyage !"
    MC "La chaleur, le sable, pas de doute, je suis de retour aux pyramides."

    jump start

label peinture_hesitation:
    MC "Euh, je sais pas trop…"
    P "Laissez-moi vous convaincre !"
    P "Voici une de mes récentes peintures,{w=0.3} vous m’en direz des nouvelles."
    # Insérer l'image avec un fondu
    show peinture with Dissolve(1.0)
    # Attendre un clic de l'utilisateur
    pause
    MC "Il a un certain talent, c’est indéniable."
    MC "Ce n’est peut-être pas une mauvaise idée au final."
    hide peinture with Dissolve(1.0)
    MC "Bon, c’est d’accord."
    P "Super !{w=0.3} Pourriez-vous vous mettre ici ?"
    P "Dans quel endroit vous voudriez je vous peigne ?"
    P "Je vais vous peindre par dessus cette esquisse du musée que j’ai commencé hier soir."
    P "Je commence."
    scene defor_1
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    MC "Je me sens bizarre…"
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "Vous dégagez un air vraiment très particulier."
    MC "Comme si je partais…"
    $ renpy.pause(1.5)
    # Transition ou effet + Attendre un peu
    P "J’approche de la fin."
    $ renpy.pause(1.5)
    # Attendre un peu
    P "Voilà qui est fait !"
    P "Bon voyage !"
    jump start
