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

  Geocode.fromLatLng("48.8583701", "2.2922926").then(
    (response) => {
      const address = response.results[0].formatted_address;
      console.log(address);
    },
    (error) => {
      console.error(error);
    }
  );

  Geocode.fromAddress("Paris").then(
    (response) => {
      const { lat, lng } = response.results[0].geometry.location;
      console.log(lat, lng);
    },
    (error) => {
      console.error(error);
    }
  );

  const [loc, setLoc] = useState("Paris");
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

  

  const sendToBack = async () => {
    const url = "http://127.0.0.1:8000/api/day";
    const res = await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        loc: loc,
        date: date,
      }),
}) 
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

          <Search getLoc={getLoc} getDate={getDate} sendToBack={sendToBack}/>
          <Map loc={loc} test={[]}></Map>

      </div>
      
    );

};

export default App;