import React, { useEffect, useState } from 'react'
import { MapContainer, TileLayer,  Marker, Popup } from 'react-leaflet';
import * as L from 'leaflet';


export default function Map(props){
  const [mapRef, setMapRef] = useState(null);

  useEffect(() => {
    if ( mapRef ){
    mapRef.flyTo({lat : props.lat, lng : props.lng});
    }
  }, [mapRef, props.lat, props.lng]);
  
  const icon = L.icon({
    iconUrl: require('./img/game.png'),
    iconSize:     [38, 38], // size of the icon
    iconAnchor:   [19, 39], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -39] // point from which the popup should open relative to the iconAncho
  })

    return (
      <div className='w-screen h-screen'>
      <MapContainer
        center={[props.lat, props.lng]}
        zoom={12}
        scrollWheelZoom={false}
        ref={(map) => setMapRef(map)}
        className="aspect-square max-w-3xl mx-auto rounded-full border-4 border-solid border-orange-950"
      >
        <TileLayer
          url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
        />

        {/* {props.res.map((el) => ( <Marker position={[el.gymnase.lat, el.gymnase.long]} icon={icon}>
          <Popup className="rounded-xl shadow-lg flex flex-col space-y-3">
            <h1 className='text-lg'>{el.gymnase.nom}</h1>
            <hr/>
            <p className='text-sm'>
              <ul>
                <li>{el.nom_eq_dom} vs {el.nom_eq_ext}</li>
                <li>à {el.gymnase.ville}</li>
              </ul>
            </p>
          </Popup>
        </Marker>
        ))
        } */}
        <Marker position={[props.lat, props.lng]} icon={icon}>
          <Popup className="rounded-xl shadow-lg flex flex-col space-y-3">
            <h1 className='text-lg'>{props.loc}</h1>
            <hr/>
            <p className='text-sm'>
              <ul>
                <li>à 16h</li>
                <li>{props.loc}</li>
              </ul>
            </p>
          </Popup>
        </Marker>
      </MapContainer>
      </div>
    );
  }
