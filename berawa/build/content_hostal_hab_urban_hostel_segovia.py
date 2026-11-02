# Contenido de la demo Häb Urban Hostel (Segovia) (es/en/fr/de). Hechos de habhostel.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Doble con terraza','Doble superior','Familiar abuhardillada'],'en':['Double with terrace','Superior double','Attic family room'],'fr':['Double avec terrasse','Double supérieure','Familiale mansardée'],'de':['Doppelzimmer mit Terrasse','Superior-Doppelzimmer','Familienzimmer im Dachgeschoss']}
RD={
'es':['Para 2 personas, con acceso a terraza individual, aire acondicionado frío-calor, TV LED y wifi gratuito.','Para 2 personas, o 3 con cama supletoria; balcón, aire acondicionado frío-calor, TV LED y suelos de madera.','Doble abuhardillada en dos plantas para 4 personas, o 5 con cama supletoria.'],
'en':['For 2 people, with access to a private terrace, hot-cold air conditioning, LED TV and free wifi.','For 2 people, or 3 with an extra bed; balcony, hot-cold air conditioning, LED TV and wooden floors.','A two-floor attic room for 4 people, or 5 with an extra bed.'],
'fr':['Pour 2 personnes, avec accès à une terrasse individuelle, climatisation chaud-froid, TV LED et wifi gratuit.','Pour 2 personnes, ou 3 avec lit d’appoint ; balcon, climatisation chaud-froid, TV LED et parquet.','Chambre mansardée sur deux niveaux pour 4 personnes, ou 5 avec lit d’appoint.'],
'de':['Für 2 Personen, mit Zugang zu einer eigenen Terrasse, Klimaanlage (warm/kalt), LED-TV und kostenlosem WLAN.','Für 2 Personen oder 3 mit Zustellbett; Balkon, Klimaanlage (warm/kalt), LED-TV und Holzböden.','Zweistöckiges Dachzimmer für 4 Personen oder 5 mit Zustellbett.']}
ART={
'hero':('columns',2211,['#1d2430','#5b6f8f','#e9eef6','#475a76','#33435c','#141a23']),
'intro':('skyline',2212,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25']),
'r1':('arches',2221,['#1d2430','#6a80a2','#eef2f8','#52678a','#3a4c69','#141a23']),
'r2':('columns',2222,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25']),
'r3':('hills',2223,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g1':('skyline',2231,['#1d2430','#5b6f8f','#e9eef6','#475a76','#33435c','#141a23']),
'g2':('hills',2232,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g3':('arches',2233,['#1d2430','#6a80a2','#eef2f8','#52678a','#3a4c69','#141a23']),
'g4':('columns',2234,['#f6f2ea','#fbf9f4','#7a3b2e','#5f5850','#2e2a25'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Häb Urban Hostel · Hostel en el centro de Segovia',see_rooms='Ver habitaciones',hero_k='Segovia · Calle Cervantes, 16',hero_t='Hostel urbano en el centro de Segovia',hero_s='En un edificio rehabilitado de la calle Cervantes, a 100 m del Acueducto.',
 intro_t='Habitaciones modernas en pleno corazón de Segovia',intro_p1='La calle Cervantes une la Plaza Mayor y el Acueducto, con paseo comercial y restaurantes segovianos a pocos metros.',
 intro_p2='Decoración cuidada, elegante, moderna y urbana; todas las habitaciones son exteriores, con balcón e insonorizadas.',
 stats=['A 100 m del Acueducto','Habitaciones exteriores','Dobles y familiares','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con WC individual completo, TV LED, aire acondicionado frío-calor, wifi gratuito y suelos y techos con vigas de madera. El edificio no tiene ascensor.',
 svcs=['Habitaciones exteriores con balcón','Dos habitaciones con terraza privada','Insonorizadas','Camas supletorias','Parkings públicos cercanos','Sin ascensor'],
 loc_p='Calle Cervantes, 16 · 40001 Segovia. Teléfonos: 921 46 10 26 · 630 88 66 61. Correo: info@habhostel.com.',
 chips=['¿Qué habitaciones tenéis?','¿Dónde aparco?','¿Tenéis ascensor?','¿Cómo reservo?']),
'en':dict(title='Häb Urban Hostel · Hostel in central Segovia',see_rooms='See rooms',hero_k='Segovia · Calle Cervantes, 16',hero_t='An urban hostel in the centre of Segovia',hero_s='In a restored building on Calle Cervantes, 100 m from the Aqueduct.',
 intro_t='Modern rooms in the heart of Segovia',intro_p1='Calle Cervantes links the Plaza Mayor and the Aqueduct, with shops and Segovian restaurants a few metres away.',
 intro_p2='Careful, elegant, modern and urban decor; all rooms face outwards, with a balcony and soundproofing.',
 stats=['100 m from the Aqueduct','Exterior rooms','Doubles and family rooms','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with a full private WC, LED TV, hot-cold air conditioning, free wifi and wooden floors and beamed ceilings. The building has no lift.',
 svcs=['Exterior rooms with balcony','Two rooms with a private terrace','Soundproofed','Extra beds','Public car parks nearby','No lift'],
 loc_p='Calle Cervantes, 16 · 40001 Segovia. Phones: +34 921 46 10 26 · +34 630 88 66 61. Email: info@habhostel.com.',
 chips=['Which rooms do you have?','Where can I park?','Is there a lift?','How do I book?']),
'fr':dict(title='Häb Urban Hostel · Auberge au centre de Ségovie',see_rooms='Voir les chambres',hero_k='Ségovie · Calle Cervantes, 16',hero_t='Une auberge urbaine au centre de Ségovie',hero_s='Dans un immeuble réhabilité de la calle Cervantes, à 100 m de l’aqueduc.',
 intro_t='Des chambres modernes au cœur de Ségovie',intro_p1='La calle Cervantes relie la Plaza Mayor et l’aqueduc, avec commerces et restaurants ségoviens à quelques mètres.',
 intro_p2='Décoration soignée, élégante, moderne et urbaine ; toutes les chambres donnent sur l’extérieur, avec balcon et insonorisation.',
 stats=['À 100 m de l’aqueduc','Chambres extérieures','Doubles et familiales','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec WC privé complet, TV LED, climatisation chaud-froid, wifi gratuit, parquet et poutres apparentes. L’immeuble n’a pas d’ascenseur.',
 svcs=['Chambres extérieures avec balcon','Deux chambres avec terrasse privée','Insonorisées','Lits d’appoint','Parkings publics proches','Sans ascenseur'],
 loc_p='Calle Cervantes, 16 · 40001 Ségovie. Téléphones : +34 921 46 10 26 · +34 630 88 66 61. E-mail : info@habhostel.com.',
 chips=['Quelles chambres avez-vous ?','Où se garer ?','Y a-t-il un ascenseur ?','Comment réserver ?']),
'de':dict(title='Häb Urban Hostel · Hostel im Zentrum von Segovia',see_rooms='Zimmer ansehen',hero_k='Segovia · Calle Cervantes, 16',hero_t='Ein urbanes Hostel im Zentrum von Segovia',hero_s='In einem sanierten Gebäude in der Calle Cervantes, 100 m vom Aquädukt.',
 intro_t='Moderne Zimmer im Herzen von Segovia',intro_p1='Die Calle Cervantes verbindet die Plaza Mayor mit dem Aquädukt, mit Geschäften und segovianischen Restaurants wenige Meter entfernt.',
 intro_p2='Sorgfältige, elegante, moderne und urbane Einrichtung; alle Zimmer liegen nach außen, mit Balkon und Schallschutz.',
 stats=['100 m vom Aquädukt','Außenzimmer','Doppel- und Familienzimmer','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit eigenem WC, LED-TV, Klimaanlage (warm/kalt), kostenlosem WLAN, Holzböden und Holzbalkendecken. Das Gebäude hat keinen Aufzug.',
 svcs=['Außenzimmer mit Balkon','Zwei Zimmer mit eigener Terrasse','Schallisoliert','Zustellbetten','Öffentliche Parkhäuser in der Nähe','Kein Aufzug'],
 loc_p='Calle Cervantes, 16 · 40001 Segovia. Telefon: +34 921 46 10 26 · +34 630 88 66 61. E-Mail: info@habhostel.com.',
 chips=['Welche Zimmer gibt es?','Wo kann ich parken?','Gibt es einen Aufzug?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@habhostel.com')
D=dict(name='Häb Urban Hostel',ac='#1d2430',ac2='#7a3b2e',ac2_a11y='#6e3529',book=BOOK,around=[],foot=FOOT,
 address='Calle Cervantes, 16 · 40001 Segovia',phones=['+34 921 46 10 26','+34 630 88 66 61'],emails=['info@habhostel.com'],maps='Häb Urban Hostel, Calle Cervantes 16, 40001 Segovia',t=T)
META=dict(repo='demo-hostal-hab-urban-hostel-segovia',name='Häb Urban Hostel',legal_name='Miguel Marazuela Bella, NIF 70266522G (política de privacidad y condiciones de su web; persona física)',registry_ids=['70266522G'],
 url='https://www.habhostel.com/',domain='habhostel.com',municipality='Segovia',province='Segovia',sector='hostel urbano en el centro histórico de Segovia',
 read_at='2026-11-02T11:15:00+01:00',created_at='2026-11-02T11:15:00+01:00',built_at='2026-11-02T11:35:00+01:00',audit_date='2026-11-02T11:15:00+01:00',
 rating=dict(value=4.5,coincide=['web'],date='2026-10-29',url='https://www.google.com/maps/search/Hab+Urban+Hostel+Segovia'),
 book=dict(mode='mail',url='mailto:info@habhostel.com',note='sin motor de reservas: su web da «RESERVAS DIRECTAS» por teléfono (921 46 10 26, 616 42 03 60) y correo info@habhostel.com. Los botones Reservar de la demo abren un correo a info@habhostel.com y los teléfonos reales van en tel: (mismo criterio que San Martín, Andrín y Hey).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis ascensor?','K03'),('¿Hay habitaciones con terraza?','K04'),('¿Tenéis camas supletorias?','K05'),('¿Dónde aparco?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay wifi?','K09'),('¿Son silenciosas las habitaciones?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Está cerca del Acueducto?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Is there a lift?','K03'),('Are there rooms with a terrace?','K04'),('Do you have extra beds?','K05'),('Where can I park?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there wifi?','K09'),('Are the rooms quiet?','K10'),('What is your phone number?','K11'),('Is it close to the Aqueduct?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Y a-t-il un ascenseur ?','K03'),('Y a-t-il des chambres avec terrasse ?','K04'),('Avez-vous des lits supplémentaires ?','K05'),('Où se garer ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il le wifi ?','K09'),('Les chambres sont-elles calmes ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Est-ce près de l’aqueduc ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es einen Aufzug?','K03'),('Gibt es Zimmer mit Terrasse?','K04'),('Haben Sie Zustellbetten?','K05'),('Wo kann ich parken?','K06'),('Wo liegt das Hostel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es WLAN?','K09'),('Sind die Zimmer ruhig?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Ist es nahe am Aquädukt?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
