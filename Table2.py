create table oracle(
        id_oracle integer primary key autoincrement,
        nom_or char(50),
        niveau integer,
        phrase_typique char(50));

create table phrase1(
        nv integer references oracle(niveau),
        id_oracle integer references oracle(id_oracle),
        phrase char(50),
        id_objet integer references elt(id_objet));

create table phrase2(
        nv integer references oracle(niveau),
        id_oracle integer references oracle(id_oracle),
        phrase char(50),
        id_objet integer references elt(id_objet));
        
create table phrase3(
        nv integer references oracle(niveau),
        id_oracle integer references oracle(id_oracle),
        phrase char(50),
        id_objet integer references elt(id_objet));  
        
create table fond(
        id_fd integer,
        nom char(50) primary key,
        id_o1 integer references oracle(id_oracle),
        id_o2 integer references oracle(id_oracle),
        id_elt1 integer references elt(nom),
        id_elt2 integer references elt(nom)
        );

create table elt(
        id_objet integer primary key autoincrement,
        nom char(50),
        quantité integer
        );

create table journal(
        id integer primary key autoincrement,
        contenu char(300)
        );

insert into journal (contenu) values
        ("257/36/51\nRappel: Le boulanger à des goûts bien étranges,\nil semblerait que tout aliment putride existant serait\nun met excellent pour son palet.\nLui donner les pots de confitures centenaires si l'odeur\ndevient trop forte."),
        ("259/05/22\nLe vieux couple à  l'entrée du village ne semble\npouvoir tenir leur langue lorsque je suis là.\nJ'aimerais leur offrir un beau bouquet\nde fleurs. Les deux sont allergiques au pollen,\nquelle sublime vue cette douce vengeance ferait!")
        ;

insert into elt (nom) values
        ("du thym"),
        ("une fiole qui sent bon"),
        ("un remède"),
        ("une pierre translucide"),
        ("un petit bouquet de fleurs"),
        ("un champignon à l'odeur putride"),
        ("un livre sur le language des fleurs"),
        ("une boucle d'oreille tombée par terre"),
        ("une coccinelle"),
        ("une plume d'un oiseau bleu"),
        ("plusieurs champignons comestibles"),
        ("quelques feuilles de menthe blanche"),
        ("une pousse de ginseg doré"),
        ("un amat de petites pierres aux couleurs vives"),
        (""),
        ("");
      
insert into fond (id_fd,nom,id_elt1,id_elt2) values
        (0, "dans le jardin devant la maison",0,2),
        (1, "dans le salon",1,6),
        (2, "au bord de la forêt",10,11),
        (3, "sur un sentier, profond dans la forêt",5,13),
        (4, "sur le chemin menant à la montagne",12,9),
        (5, "près du banc, au bout du chemin",4,8),
        (6, "à l'entrée du village",3,15),
        (7, "sur la place du village",7,14);
		
		
		
		
		
		
		
		
		
