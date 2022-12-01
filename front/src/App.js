import React, {useState} from 'react';
import Search from './Search.js'
import Map from './Map.js'
import bg from "./img/bg3.jpg";
import Geocode from "react-geocode";
import moment from 'moment';

const App = () => {

    Geocode.setApiKey("AIzaSyDC9fTbYopPV742LwoJidajiI5UeUqEf4Y");
    Geocode.setLanguage("fr");
    Geocode.setRegion("fr");
    Geocode.setLocationType("ROOFTOP");

    // const formatDate = (date) => {
    //     var d = new Date(date),
    //         month = '' + (d.getMonth() + 1),
    //         day = '' + d.getDate(),
    //         year = d.getFullYear();
    
    //     if (month.length < 2) 
    //         month = '0' + month;
    //     if (day.length < 2) 
    //         day = '0' + day;
    
    //     return [year, month, day].join('-');
    // }
     

    const [loc, setLoc] = useState("Paris");
    const [lati, setLat] = useState(48.852968);
    const [lngi, setLng] = useState(2.349902);
    const [date, setDate] = useState(moment.utc().format("YYYY-MM-DD"));
    const [res, setRes] = useState([]);

    
    const getLoc = (loc) => {
        setLoc(loc)
    }

    const getDate = (date) => {
        setDate(moment.utc(date).format("YYYY-MM-DD"))
    }

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
            headers: { 
                'Content-Type': 'application/json',
                'accept' : 'application/json',
            },
            body: JSON.stringify({
                date: date,
                lat: lati,
                lng: lngi,
            }),
        });

        setRes(res.json());
        console.log(res.json());
    }

    return (
        <div className="bg-scroll bg-center bg-cover content-center space-y-10" style={{backgroundImage: `url(${bg})`}}>

            <Search getLoc={getLoc} getDate={getDate} sendToBack={sendToBack}/>
            <Map loc={loc} lat={lati} lng={lngi} res={res}></Map>

        </div>

    );

};

export default App;