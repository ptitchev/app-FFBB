import React from 'react'
import { MapContainer, TileLayer,  Marker, Popup } from 'react-leaflet';
import * as L from 'leaflet';


export default function Map(props){
  // {props.test}
  
  const icon = L.icon({
    iconUrl: require('./img/game.png'),
    iconSize:     [38, 38], // size of the icon
    // iconAnchor:   [49, 3], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -35] // point from which the popup should open relative to the iconAncho
  })

    return (
      <div className='w-screen h-screen'>
      <MapContainer
        center={[49, 3]}
        zoom={16}
        scrollWheelZoom={false}
        className="aspect-square max-w-3xl mx-auto rounded-full border-4 border-solid border-orange-950"
      >
        <TileLayer
          url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
        />
        <Marker position={[49, 3]} icon={icon}>
          <Popup className="rounded-xl shadow-lg flex flex-col space-y-3">
            <h1 className='text-lg'>Nom du match</h1>
            <hr/>
            <p className='text-sm'>
              <ul>
                <li>A vs B</li>
                <li>à 14h</li>
                <li>{props.loc}</li>
              </ul>
            </p>
          </Popup>
        </Marker>
      </MapContainer>
      </div>
    );
  }
