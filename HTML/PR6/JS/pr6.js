//Funcio espectacular
/*
function somethingToDo(frase) 
{
    //Dividim la frase per contar la cantitat de paraules 
    const divParaules = frase.split(" ");
    const paraules = divParaules.length;
    //La variable total ens retorna la totalitat de la cadena
    const total = divParaules.join("").length; 

    //Per obtenir la mitja(average) convertim a flotant i dividim el total per la cantitat
    const average =parseFloat((total/paraules).toFixed(2));
    const resultat =
    {
        paraules: paraules,
        total: total,
        average: average
    };

    console.log(resultat);
}
somethingToDo("Tenim tres paralules?");
*/
//EXERCICI 2
//La funcio SHOW tracta de mostrar (titol,numero de temporades )
class Show {
    constructor(title, numberOfSeasons, episodesPerSeason) {
      this.title = title;
      this.numberOfSeasons = numberOfSeasons;
      this.episodesPerSeason = episodesPerSeason;
  }
}

const breakingBad = new Show('Breaking Bad', 5, 12);
const gameOfThrones = new Show('Game of Thrones', 8, 9);
const theSimpson = new Show('The Simpsons', 32, 24);

const shows = [breakingBad, gameOfThrones, theSimpson];

// =================================
// Modificar el codi a partir d'ara!
// =================================
function previewShows(serie)
{
  const TitleText = serie.title;
  const SeasonsText = serie.numberOfSeasons + ' seasons';
  const EpisodesText = serie.episodesPerSeason + ' episodes per season';
  const Component = 
  {
    titleText: TitleText,
    seasonsText: SeasonsText,
    episodesText: EpisodesText
  }
  return(Component);
}

const save_breakingBad = previewShows(breakingBad);
const save_gameOfThrones = previewShows(gameOfThrones);
const save_theSimpson = previewShows(theSimpson);


const showComponents = [save_breakingBad, save_gameOfThrones, save_theSimpson];

// ============================
// Modificar el codi de sobre!!
// ============================
const body = document.querySelector('body');

function updateShows() {
  for (let show of showComponents) {
    const showPane = document.createElement('div');
    showPane.classList.add('series-frame');
    const showHeading = document.createElement('h2');
    showHeading.innerText = show.titleText;
    const showDetails = document.createElement('p');
    const seasons = document.createElement('p');
    seasons.innerText = show.seasonsText;
    const episodes = document.createElement('p');
    episodes.innerText = show.episodesText;
    showDetails.append(seasons);
    showDetails.append(episodes);
    showPane.append(showHeading);
    showPane.append(showDetails);
    body.append(showPane);
  }
};

updateShows();