import React , { Component }from 'react'
import { MapContainer, TileLayer,  Marker, Popup } from 'react-leaflet';


class SimpleMap extends Component {
  render() {
    return (
      <div className='w-screen h-screen'>
      <MapContainer
        center={[49, 3]}
        zoom={20}
        maxZoom={10}
        attributionControl={true}
        zoomControl={true}
        className="aspect-square max-w-3xl mx-auto rounded-full border-4 border-solid border-orange-600"
      >
        <TileLayer
          url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
        />
        <Marker position={[49, 3]}>
          <Popup>
            Popup for any custom information.
          </Popup>
        </Marker>
      </MapContainer>
      </div>
    );
  }
}

export default SimpleMap