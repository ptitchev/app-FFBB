import { Popup, Marker } from 'react-leaflet';
import * as L from 'leaflet';


export default function MarkerCu(props){

    const icon = L.icon({
        iconUrl: require('./img/game.png'),
        iconSize:     [38, 38], // size of the icon
        iconAnchor:   [49, 3], // point of the icon which will correspond to marker's location
        popupAnchor:  [-3, -30] // point from which the popup should open relative to the iconAncho
      })
    
    return (
        <Marker position={[49, 3]} icon={icon} className="">
          <Popup>
            Popup for any custom information.
          </Popup>
        </Marker>
    )

}   