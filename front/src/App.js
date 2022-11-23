import React from 'react';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
        day: ""
    };
  }

  async componentDidMount() {
      const res = await fetch('http://127.0.0.1:8000/api/day')
      const res_json = await res.json()
      console.log(res_json)
      this.setState({'day': res_json})
  }
  

  render() {
    return <h1 className="text-xl font-medium text-yellow">Hey!  It's {this.state.day}</h1>;
  }

}

export default App;