<?php
 include_once("configuration.php");
 include_once("tete.php");
 include_once("bouttons.php");
?>
    
    <H1>Documentation pour F.O.I.</H1>
    <H1><em>Cette doc doit être réécrite dans la nouvelle version</em></H1>
    <hr width="30%">
    <h2>Les pages d'aministration</H2>
    Les pages suivantes sont disponibles:
    <ul>
    <li><a href="index.php">Accueil</A> : page d'entrée, on voit l'état du serveur, mais on ne peut rien changer<br/>
        les liens sont tous actifs, et ouvent une nouvelle fenêtre.</li>
    <li><a href="site.php">Accès</A> : permet de déterminer quelles pages du site publique sont visibles et quelles pages sont cachées<br/>
        permet de choisir quelle film sera mis à part en tête de la liste (le reste de liste reste anti-chronologique)<br/>
        Pour enlever cette information, il suffit de cocher un film non-visible, et ca disparaît à la mise à jour.<br/> </li>
    <li><a href="content.php">Contenu</A> : permet de modifier les pages du site publique, ainsi que leur contenu.<br/>
        pour l'instant, seul le recalcul est possible, la modification du contenu ne marche pas.</li>
    <li><a href="stat.php">Statistiques</A> : permet de suivre l'accès du site : téléchargements, visites, charge, etc...<br/>
        ne pas hésiter à fouiller.</li>
    <li><a href="diag.php">Diagnostic</A> : permet de voir les messages d'erreur, si il y en a.<br/>
        plus difficile d'accès, sert surtout aux développeurs du site.</li>
    </ul>
    <hr width="30%">
    <h2>Plan succinct de ce site</H2>
    Cette organisation est temporaire, en attendant l'ouverture du site.
    <ul>
    <li><a href="http://www.netforgod.tv">http://www.netforgod.tv</a><br/>
        page présentant la video du mois
    </li>
    <li><a href="http://www.netforgod.tv/VOD">http://www.netforgod.tv/VOD</a><br/>
        La page permettant la VOD. Existe en Français et en anglais<BR/>
        page normalement en accès libre <BR/>
        Page de garde
        </li>
    <li><a href="http://www.netforgod.tv/FOI">http://www.netforgod.tv/FOI</a><br/>
        La page permettant pour les groupes. Existe seulement en Français</li>
        page normalement en accès libre (pas encore écrite)
    <li><a href="http://www.netforgod.tv/FOI/download">http://www.netforgod.tv/FOI/download</a><br/>
        La page pour le téléchargement de la video du mois en "HD". Page bilingue Français/Anglais<BR/>
        page normalement accessible à tous les responsables FOI
    </li>
    <li><a href="http://www.netforgod.tv/FOI/FOI_07_10">http://www.netforgod.tv/FOI/FOI_YY_MM</a><br/>
        La page pour le téléchargement de la video YY/MM en "HD". Page bilingue Français/Anglais<BR/>
        pages normalement fermées, sauf cas particulier
    </li>
    <li><a href="http://www.netforgod.tv/prgm">http://www.netforgod.tv/prgm</a><br/>
        Les pages d'administration<BR/>
        pages seulement accessible aux administrateurs
    </li>
    </ul>
        <hr width="30%">
    <h2>Principe d'organisation</h2>

    <p>Description du flux de traitement automatique développé pour fournir rapidement les vidéo sur le serveur.</p>

    <p>le but est de partir de fichiers proches de la production (DVD , fichiers mpg, fichers wav ou ac3) et de produire des fichiers utilisables sur le serveur WEB : divx de bonne qualité pour le téléchargement et video flash pour la Video à la demande, et la télé en ligne.</p>

    <p>Le principe est que le traitement des différents fichiers est pris automatiquement en charge par des scripts lancés automatiquement à intervalle régulier. Tout se base sur l'utilisation de noms standards des différents fichiers.
        Deux machines sont concernées :<br/>
        <b>la machine de PostProduction</b> : Saul (machine rapide sous linux, au 59)<br/>
        <b>le serveur</b> : une dedibox : <a href="http://www.netforgod.tv">www.netforgod.tv</a> .</p>


        <hr width="30%">
     <h2>Fichiers à créer sur la machine de PostProduction</h2>
    <p>il faut créer les fichiers sur la machine de PostProduction :</p>
    <blockquote>
    <p> les noms de <span class="ex_it">dossiers</span> sont en surlignés italique; le nom de <span class="ex">fichiers</span> sont surlignés<br/>
    les <b>fichiers</b> marqués en gras n'ont pas à être créés, ils sont calculés automatiquement par le programme
    </p>
    </blockquote>
    <ul>
    <li><span class="ex_it">export</span></li>
    <ul>
        <li><span class="ex_it">FOI_YY_MM</span>     où YY est le numéro de l'année et MM est le numéro du mois (01 à 12) il y a autant de dossier que nécessaire.</li>
        <ul>
            <li><span class="ex">video.mpg</span>     la video, sans le son, en qualité optimale</li>
            <li><span class="ex">affiche.jpg</span>     une image affiche de la vidéo, en format 320x240 pixel ou 640x480</li>
            <li><b>video.avi</b>     la vidéo, sans le son, en qualité divx, codec XVID / DIVX</li>
            <li><b>LL_divx.avi</b>     la video en format divx dans la langue LL - <i>fichier optionnel</i></li>
        </ul>
        <ul>
            <li><span class="ex_it">sons</span></li>
            <ul>
                <li><span class="ex">LL.wav</span>     le son dans la langue LL (code ISO à 2 - ou parfois 3 - lettres;</li>
                <li><b>LL.ac3</b>     le son en format .ac3 ( peut-être utilisé pour créer un DVD)</li>
                <li><b>LL.mp3</b>     le son en format .mp3</li>
                <li>voir à <a href="http://en.wikipedia.org/wiki/List_of_ISO_639-2_codes">ICI</a> pour les codes des langues</li>
            </ul>
            <li><span class="ex_it">textes</span></li>
            <ul>
                <li><span class="ex">titre_LL.txt</span>     le titre dans la langue LL (le français et l'anglais sont seuls nécessaires)</li>
                <li><span class="ex">resume_LL.txt</span>     le résumé du film  dans la langue LL (le français et l'anglais sont seuls nécessaires)</li>
            </ul>
            <li><span class="ex_it">images</span></li>
            <ul>
                <li><span class="ex">photoxx.jpg</span>  les photos extraites du film, numérotées par ordre d'apparition dans le diaporama</li> 
                <li><span class="ex">photoxx_LL.txt</span>  les légendes des photos avec les mêmes noms</li>
                ou bien
                <li><span class="ex">legendes_LL.txt</span>  les légendes des photos tout dans un seul fichier (<em>pas en core actif</em>)</li>
                <pre>
            photo01 : texte de la légende
            photo02 : texte de la légende
            etc.
                </pre>
                <i>si photoxx_LL.txt ET legendes_LL.txt sont présents en même temps, c'est les photoxx_LL.txt qui sont choisit</i>
            </ul>
            <li><span class="ex">public</span> (fichier vide) éventuellement, si cette vidéo doit être mise sur la page de VOD</li>
            <li><span class="ex">parametres.xml</span> un fichier contenant des paramètres supplémentaires pour le codage</li>
			<ul>Les paramètres utilisés sont :
				<li><tt>aspect</tt> : le format dy film; soit <tt>4:3</tt> soit <tt>16:9</tt> - 4:3 est utilisé par défaut</li>
				<li><tt>start_at</tt> : le point de début du film utilisé pour la version VOD, généralement la durée du générique - 47 secondes sont prises par défaut.</li>
				<li><tt>excerpt</tt> : <tt>True/False</tt>, si <tt>True</tt>, un extrait sera créé, et présenté sur la page de garde - <tt>False</tt> par défaut (<em>pas en core actif</em>)</li>
				<li><tt>excerpt_beg</tt> : le point de début utilisé pour faire l'extrait, en secondes; valeur par défaut = 120</li>
				<li><tt>excerpt_end</tt> : le point de fin utilisé pour faire l'extrait, en secondes; valeur par défaut = 165 </li>
				<li>Voici un exemple de fichier <tt>parametres.xml</tt> (attention, les détails de ce fichier sont importants (les &lt; &gt; / " et autres caratères) )</li>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!-- contient les paramètres optionnels du film --&gt;
&lt;FOI_MOVIE>
	&lt;start_at value="45"/&gt;
	&lt;aspect value="16:9"/&gt;
	&lt;excerpt value="True"/&gt;
	&lt;excerpt_beg value="1147"/&gt;
	&lt;excerpt_end value="1223"/&gt;
&lt;/FOI_MOVIE&gt;
</pre>
			</ul
        </ul>
    </ul>
    </ul>
    <hr width="30%">
    
    <h2>Fonctionnement général du programme</h2>
    <ul>
        <li>sur la machine de PostProduction</li>
    <p>Un programme <span class="ex">Makefile</span> contient toute les commandes pour réaliser les transformations nécessaires.
         Ce programme est exécuté automatiquement toute les heures, et crée <b>les fichiers marqués en gras</b> puis lance le transfert des nouveaux fichiers vers le serveur</p>
    <p>Le plus simple est de laisser la machine tourner toute seule. Cette machine peut-être éteinte quand il n'y a pas de nouveaux fichiers à poser.</p>

    <li>sur le serveur</li>
    <p>Sur le serveur on retrouve une architecture similaire, mais les fichiers sont un peu différents.
        Certains fichiers ne sont pas transférés (les fichiers .mpg .ac3 et .wav) car gros et inutiles sur le serveur;
        D'autres sont créés sur le serveurs : les pages WEB, les videos basses résolutions, etc...</p>
    <p> On y trouve les pages suivantes :
    <ul>
        <li>Pages de VOD (Video On Demand) <a href="http://www.netforgod.tv/VOD">www.netforgod.tv</A></li>
            on n'y trouve que les video "publique" (celles qui ont le fichier "public")
        <li>Pages de téléchargement www.netforgod.tv/FOI/FOI_YY_MM</A></li>
            toutes les video, même celles qui ne sont pas publiques
        <li>ces pages d'administrations</li>
    </ul>
    Ces pages sont calculées automatiquement toute les heures.
    </ul>

    <hr width="30%">
    <h2>Fonctionnement Détaillé du programme - <em>Pour les programmeurs</em> -</h2>
    <ul>
        <li>sur la machine de PostProduction</li>
        <ul>
    <li>Le programme <span class="ex">Makefile</span> contient toute les commandes pour réaliser les transformations nécessaires. Ce programme est exécuté en utilisant la commande  <tt>make ''arguments''</tt> . Plusieurs commandes sont possibles, dont <tt>make help</tt> qui donne une documentation complète. La commande la plus importante est <tt>make all</tt>. Elle est appelée automatiquement toute les heures, et crée <b>les fichiers marqués en gras</b> puis lance le transfert.</li>
    <li>on trouve de la doc sur make <a href="http://www.gnu.org/software/make/manual/html_node/index.html">ICI</a></li>

    <li>A la fin des transformations, les fichiers sont transférés sur le serveur par la commande rsync, en comparant les dates. 
        Si un fichier est absent sur le serveur, ou si le fichier sur le serveur est plus ancien que celui de la machine de PostProd. il est recopié
        Sauf pour les fichiers divx qui ne sont pas transférés, mais recréés sur le serveur (ca va plus vite).</li>
    <li>Pour que ca marche il faut avoir installé sur la machine de PostProd :</li>
        <ul>
            <li>FFMPEG relativement à jour - ce programme fait les transformations des sons et des videos -</li>
            <li>un certificat ssh permettant à cette machine de se connecter directement sur le serveur </li>
            <li>des outils standards : make; rsync ... (standard Linux)</li>
        </ul></ul>

    <li>sur le serveur</li>
    <ul>
        <li>Sur le serveur, on retrouve une organisation similaire</li>
        <li><span class="ex_it">$WEBROOT/</span>racine du site</li>
        <ul>
            <li><span class="ex_it">videos</span> le dépot de fichier de référence, c'est là que sont recopié les fichiers de la machine de PostProd, protégé par mot de passe (<strong>.htaccess</strong>) et normalement inaccessible </li>
            <ul>
                <li><span class="ex_it">FOI_YY_MM</span>     où YY est le numéro de l'année et MM est le numéro du mois (01 à 12) il y a autant de dossier que nécessaire.</li>
                <ul>
                    <li><span class="ex">video.avi</span> le fichier image en divx haute qualité</li>
                    <li><span class="ex">public</span> la présence de ce fichier indique que ce film doit être mis dans la page publique</li>
                    <li><span class="ex_it">sons</span> un dossier avec tout les sons</li>
                    <ul>
                        <li><b>LL.mp3</b> les sons dans toutes les langues</li>
                    </ul>
                    <li><b>LL_divx.avi</b> les films DivX dans toutes les langues</li>
                    <li><b>LL_divx.flv</b> les films flash dans toutes les langues</li>
                    <li><span class="ex_it">textes</span> comme sur la machine de PostProd</li>
                    <li><span class="ex_it">images</span> comme sur la machine de PostProd</li>
                    <li><span class="ex_it">thumbs</span> les vignettes des images dans images/ </li>
                    <li><b>affiche.jpg index.html presentation.html diaporama.html ...</b> des fichiers utilisés pour le site</li>
                    <li><b>dl.php, dl.log</b> le programme qui réalise le téléchargement, avec son log</li>
                </ul>
            </ul>
            <li><span class="ex_it">FOI</span> la zone pour les groupes F.O.I, protégé par mot de passe (<strong>.htaccess</strong>) et réservée aux responsables.</li>
            <ul>
                <li>on retrouve la même organisation que dans videos/, <strong>sauf que</strong> </li>
                <li>les directories <span class="ex_it">FOI_YY_MM</span> sont des "liens soft" (ln -s) vers ../videos/. Cela permet de découpler le contenu (videos/) avec ce qui est disponible sur le site (FOI/).</li>
                <li><span class="ex_it">download</span> est un lien soft vers le téléchargement actuel</li>
            </ul>
            <li><span class="ex_it">VOD</span> la zone publique</li>
            <ul>
                <li><span class="ex">index.html index_en.html</span>     les pages d'accueil grand public.</li>
            </ul>
            <li><span class="ex_it">prgm</span> Les programmes d'administration'</li>
            <ul>
                <li>tous les scrits python, Makefile pour la maintenance automatique des pages</li>
                <li>les fichiers .php du back-office (ici même)</li>
            </ul>
        </ul>
        <li>Tout ca est maintenu par un jeu de programmes appelé toutes les heures</li>
        <ul>
            <li><span class="ex">auto.sh</span> est appelé par cron, c'est lui qui appelle les autres programmes'</li>
            <li><span class="ex">do_vod.py</span> un script python qui fabrique <b>VOD/index.html</b> à partir des éléments disponibles dans le file-système</li>
            <li><span class="ex">do_tele.py</span> un script python qui fabrique les <b>FOI_YY_MM/index.html</b> à partir des éléments disponibles dans le file-système</li>
            <li><span class="ex">Makefile</span> s'occupe des dépendances des différents fichiers, en particulier les .flv</li>
	</ul>
	<li>Pour ca il faut avoir installer les programes suivants :</li>
	<ul>
	  <li>python 2.5</li>
	  <li>ffmpgeg, avec le codec flash intégré</li>
	  <li>les outils standards (make, ...)</li>
	</ul>
    </ul>
    </ul>

    <hr width="30%">
    <h2>Si on est pressé</h2>
    <p>Ce fonctionnement automatique implique que ca met un certain temps.
    Entre le moment où un fichier son est posé sur la machine de PostProduction, et l'apparition de la vidéo dans la page de VOD, ca peut prendre jusqu'à quelques heures.</p>
    <p>En particulier, si un téléchargement est urgent, il vaut mieux mettre la langue seule, et attende 1 heure pour mettre les langues moins urgentes</p>
    <p>Si on est <b>très</b> pressé, il faut poser une langue dans le dossier sons, et au niveau du dossier <span class="ex_it">export</span>, faire :
        <pre>
        make all
        </pre>
    dans ce cas, le calcul est lancé au moment même.
    On gagne en moyenne une demi-heure avec ce système.
    </p>
    <hr width="30%">
</body>
</html>