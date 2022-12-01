import React, {useState} from 'react';
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
    const [res, setRes] = useState([]);


    const getLatLng = async () => {
        const response = await Geocode.fromAddress(loc)
        const {lat, lng} = response.results[0].geometry.location;
        setLat(lat)
        setLng(lng)
    }

    const sendToBack = async () => {

        await getLatLng()
        const url = "http://127.0.0.1:3001/api/request";
        const res = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                date: date,
                lat: lati,
                lng: lngi,
            }),
        });

        setRes(res.json());
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
            <Map loc={loc} lat={lati} lng={lngi} res={res}></Map>

        </div>

    );

};

export default App;