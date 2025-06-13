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
    style: 'mapbox://styles/mapbox/satellite-streets-v12', // Using satellite with minimal streets for better tile availability
    use3dTerrain: true, //set true for enabling 3D maps.
    auto: false,
    title: 'Ukraine War News',
    subtitle: 'Latest updates from the frontline',
    byline: 'Data from LiveUAMap',
    footer: 'Source: LiveUAMap news data <br> Created using <a href="https://github.com/mapbox/storytelling" target="_blank">Mapbox Storytelling</a> template.',
    newsDataPath: 'http://localhost:8080/news-ak-optimized.json', // Path to the JSON file containing news data
    defaultZoom: 6,
    defaultCenter: [31.1656, 48.3794], // Center of Ukraine
    chapters: [
        {
            id: 'default-view',
            alignment: 'center',
            hidden: false,
            title: '',
            description: '',
            location: {
                center: [31.1656, 48.3794], // Center of Ukraine
                zoom: 6,
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
