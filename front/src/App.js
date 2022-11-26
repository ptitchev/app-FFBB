import React, {useEffect, useState} from 'react';
import Search from './Search.js'
// import Map from './Map.js'
import SimpleMap from './Map.js'
// import Navbar from './Navbar.js';
import bg from "./img/bg3.jpg";

const App = () => {

  // const mapIsReadyCallback = (map) => {
  //   console.log(map);
  // };

  const [loc, setLoc] = useState("");

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

    return (
      <div className="bg-scroll bg-center bg-cover content-center space-y-16" style={{backgroundImage: `url(${bg})`}}>

          <Search/>
          <SimpleMap></SimpleMap>

      </div>
      
    );

};

export default App;