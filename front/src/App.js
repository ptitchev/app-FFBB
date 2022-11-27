import React, {useEffect, useState} from 'react';
import Search from './Search.js'
import Map from './Map.js'
import bg from "./img/bg3.jpg";
import Geocode from "react-geocode";

const App = () => {

  Geocode.setApiKey("AIzaSyDC9fTbYopPV742LwoJidajiI5UeUqEf4Y");
  Geocode.setLanguage("fr");
  Geocode.setRegion("fr");
  Geocode.setLocationType("ROOFTOP");

  const [loc, setLoc] = useState("Paris");
  const [lati, setLat] = useState(48.852968);
  const [lngi, setLng] = useState(2.349902);
  const [date, setDate] = useState(Date.now());

    useEffect(() => {
        const url = "http://127.0.0.1:8000/api/day";

        const fetchData = async () => {
            try {
                const res = await fetch(url);
                const res_json = await res.json();
                setLoc(res_json);
            } catch (error) {
                console.log("error", error);
            }
        };

        fetchData();
    }, []);

  const getLatLng = async () => {
    console.log("test : ", loc)
    const response = await Geocode.fromAddress(loc)
    console.log("test : ", response)
    const { lat, lng } = response.results[0].geometry.location;
    console.log(lat, lng);
    setLat(lat)
    setLng(lng)
  }

  const sendToBack = async () => {

    getLatLng()
  //   const url = "http://127.0.0.1:8000/api/day";
  //   const res = await fetch(url, {
  //     method: "POST",
  //     body: JSON.stringify({
  //       loc: loc,
  //       date: date,
  //     }),

  // }) 
  }

  const getLoc = (loc) => { 
    setLoc(loc)
    console.log(loc)
  }

  const getDate = (date) => { 
    setDate(date)
    console.log(date)
  }



  

    return (
      <div className="bg-scroll bg-center bg-cover content-center space-y-10" style={{backgroundImage: `url(${bg})`}}>

          <Search getLoc={getLoc} getDate={getDate} sendToBack={sendToBack} />
          <Map loc={loc} lat={lati} lng={lngi} test={[]}></Map>

      </div>
      
    );

};

export default App;