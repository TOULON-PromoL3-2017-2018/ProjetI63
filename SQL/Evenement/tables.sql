CREATE TABLE Universite (
  NoUniversite INTEGER PRIMARY KEY,
  NomUniversite VARCHAR(30) NOT NULL,
  Ville VARCHAR(30) NOT NULL,
  Rue VARCHAR(30) NOT NULL,
  Arrondissement VARCHAR(30),
  Contact VARCHAR(30) NOT NULL
);

CREATE TABLE ParticipantAsso (
  NoParticipantAsso INTEGER PRIMARY KEY,
  NoUniversite INTEGER REFERENCES Universite,
  NoEtudiant INTEGER REFERENCES Etudiant --partie Xavier
);

CREATE TABLE ParticipantAutre (
  NoParticipantAutre INTEGER PRIMARY KEY,
  NoUniversite INTEGER REFERENCES Universite,
  NomEtudiantAutre VARCHAR(20) NOT NULL,
  PrenomEtudiantAutre VARCHAR(20) NOT NULL,
  MailEtudiantAutre VARCHAR(40) NOT NULL,
  TelephoneAutre VARCHAR(20) NOT NULL,
  NoEtudiantAutre INTEGER NOT NULL
);

CREATE TABLE Presse (
  NoPresse INTEGER PRIMARY KEY,
  Organisme VARCHAR(20) NOT NULL
);

CREATE TABLE Personnel (
  NoPersonnel INTEGER PRIMARY KEY,
  NomPersonnel VARCHAR(20) NOT NULL,
  PrenomPersonnel VARCHAR(20) NOT NULL
);

CREATE TABLE Type (
  NoTypeEvenement INTEGER PRIMARY KEY,
  TypeEvenement VARCHAR(20) NOT NULL
);

CREATE TABLE Sport (
  NoSport INTEGER PRIMARY KEY,
  NomSport VARCHAR(20) NOT NULL,
  TypeSport VARCHAR(20) NOT NULL,
  NbJoueursMini INTEGER NOT NULL
);

CREATE TABLE EvenementSport (
  NoEvenementSport INTEGER PRIMARY KEY,
  NoSport INTEGER REFERENCES Sport,
  NoVainqueur INTEGER,
  Score VARCHAR(20),
  RecompenseVainqueur INTEGER,
  NombreSpectateur INTEGER
);

CREATE TABLE Evenement(
  NoEvenement INTEGER PRIMARY KEY,
  NoPersonnel INTEGER REFERENCES Personnel,
  NoTypeEvenement INTEGER REFERENCES Type,
  NoPresse INTEGER REFERENCES Presse,
  NoEvenementSport INTEGER REFERENCES EvenementSport,
  DateEvenement DATE NOT NULL,
  VilleEvenement VARCHAR(20),
  PrixEvenement INTEGER NOT NULL,
  DureeEvenement INTEGER NOT NULL,
  PrixPlace INTEGER NOT NULL,
  Notation INTEGER NOT NULL
);

CREATE TABLE InscritAsso (
  NoParticipantAsso INTEGER REFERENCES ParticipantAsso,
  NoEvenement INTEGER REFERENCES Evenement,
  PRIMARY KEY (NoParticipantAsso, NoEvenement)
);

CREATE TABLE InscritAutre (
  NoParticipantAutre INTEGER REFERENCES ParticipantAutre,
  NoEvenement INTEGER REFERENCES Evenement,
  PRIMARY KEY(NoParticipantAutre, NoEvenement)
);
