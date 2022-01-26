%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%                                  %%%
%%%  Format de style pour les cours  %%%
%%%                                  %%%
%%%        Vincent Croizier          %%%
%%%                                  %%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{PMCours}[2016/07/09 style de cours pour les prépas]

%%%  Chargement de la classe article, avec transfert d'options
\PassOptionsToClass{a4paper}{article}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions

\LoadClass{article}


%%%  Chargement des Packages
\RequirePackage{PMCours}

%%%  Destination de l'article (proposé pour une conf, une revue...)

\def\Destination#1{\ifx{#1}{}\gdef\@Destination{}%
\else\gdef\@Destination{#1}\fi}

%%%   Destination vide par défaut

\Destination{}
