var config = {
    // style: 'mapbox://styles/mapbox/streets-v12',
    // leave commented to use Mapbox Standard Style
    accessToken: 'pk.eyJ1Ijoic3R0ZGV4IiwiYSI6ImNsaGtwOXE0NTB1N2Ezbm9lZmNjZ210ejMifQ.8PmZcJ-9gEMolQoDZd2NKQ',
    showMarkers: true,
    markerColor: '#3FB1CE',
    //projection: 'equirectangular',
    //Read more about available projections here
    //https://docs.mapbox.com/mapbox-gl-js/example/projections/
    inset: true,
    insetOptions: {
        markerColor: 'orange'
    },
    insetPosition: 'bottom-right',
    theme: 'dark',
    style: 'mapbox://styles/mapbox/satellite-streets-v12',
    use3dTerrain: true, //set true for enabling 3D maps.
    auto: false,
    title: 'Frontline updates from General Staff of the Ukrainian Armed Forces',
    subtitle: 'Author: Stanislav Pavliuk',
    byline: 'Data from <a href="https://liveuamap.com/">LiveUAMap</a> and <a href="https://deepstatemap.live/">DeepStateMap</a>.',
    footer: 'Source: LiveUAMap news data <br> Created using <a href="https://github.com/mapbox/storytelling" target="_blank">Mapbox Storytelling</a> template.',
    newsDataPath: 'news-ak-optimized.json',
    defaultZoom: 4,
    defaultCenter: [31.1656, 48.3794],
    chapters: [
        {
            id: 'default-view',
            alignment: 'center',
            hidden: false,
            title: '',
            description: '',
            location: {
                center: [31.1656, 48.3794],
                zoom: 5,
                pitch: 30,
                bearing: 0
            },
            mapAnimation: 'flyTo',
            rotateAnimation: false,
            callback: '',
            onChapterEnter: [],
            onChapterExit: []
        }
    ]
};
