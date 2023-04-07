import React from 'react'; 
import axios from 'axios';

class App extends React.Component { 
	state = {
		details: [],
	}
	
	componentDidMount() {
		let data;
		
		axios.get('http://localhost:8000/wel/').then(res => {
			data = res.data;
			this.setState({
				details:data
			})
		})
		.catch((err) => {
			console.log(err)
		})
	}

	handleInput = (e) => {
		this.setState({
			[e.target.treatment]: e.target.value,
		})
	}

	handleSubmit = (e) => {
		e.preventDefault();
		
		axios.post("http://localhost:8000/wel/", {
			date: this.state.day,
			patient: this.state.patient,
			doctor: this.state.doctor,
			diagnosis: this.state.diagnosis,
			treatment: this.state.treatment,
			rand_id: this.state.rand_id
		}).then((res) => {
			this.setState({
				day: "",
				patient: "",
				doctor: "",
				diagnosis: "",
				treatment: "",
				rand_id: ""
			})
		}).catch((err) => {
			console.log(err.response)
		})
	}

    render() { 
        return(
            <div className="container jumbotron ">
				<form onSubmit={this.handleSubmit}>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text"
                                  id="basic-addon1">
                                {" "}
                                Today's Date{" "}
                            </span>
                        </div>
                        <input type="date" className="form-control" 
                               placeholder="Date of Prescription"
                               aria-label="Date"
                               aria-describedby="basic-addon1"
                               value={this.state.day} name="day"
                               onChange={this.handleInput} />
                    </div>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text">
                               PatientId 
                            </span>
                        </div>
                        <textarea className="form-control " 
                                  aria-label="With textarea"
                                  placeholder="Patient Wallet" 
                                  value={this.state.patient} name="quote" 
                                  onChange={this.handleInput}>
                        </textarea>
                    </div>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text">
                               Diagnosis
                            </span>
                        </div>
                        <textarea className="form-control " 
                                  aria-label="With textarea"
                                  placeholder="Diagnosis" 
                                  value={this.state.diagnosis} name="quote" 
                                  onChange={this.handleInput}>
                        </textarea>
                    </div>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text">
                               Treatment
                            </span>
                        </div>
                        <textarea className="form-control " 
                                  aria-label="With textarea"
                                  placeholder="Treatment" 
                                  value={this.state.treatment} name="quote" 
                                  onChange={this.handleInput}>
                        </textarea>
                    </div>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text">
                               Rand Id
                            </span>
                        </div>
                        <input type="number" className="form-control" 
                               placeholder="Random ID"
                               aria-label="Rand"
                               aria-describedby="basic-addon1"
                               value={this.state.rand} name="day"
                               onChange={this.handleInput} />
                    </div>
					<div className="input-group mb-3">
                        <div className="input-group-prepend">
                            <span className="input-group-text">
                               Doctor Id
                            </span>
                        </div>
                        <textarea className="form-control " 
                                  aria-label="With textarea"
                                  placeholder="Doctor Wallet" 
                                  value={this.state.doctor} name="quote" 
                                  onChange={this.handleInput}>
                        </textarea>
                    </div>
  
                    <button type="submit" className="btn btn-primary mb-5">
                        Submit
                    </button>
				</form>
				<hr
                    style={{
                        color: "#000000",
                        backgroundColor: "#000000",
                        height: 0.5,
                        borderColor: "#000000",
                    }}
                />

				{this.state.details.map((detail, id) => (
                    <div key={id}>
                        <div className="card shadow-lg">
                            <div className={"bg-" + this.renderSwitch(id % 6) + 
                                          " card-header"}>Quote {id + 1}</div>
                            <div className="card-body">
                                <blockquote className={"text-" + this.renderSwitch(id % 6) + 
                                                   " blockquote mb-0"}>
                                    <h1> {detail.detail} </h1>
                                    <footer className="blockquote-footer">
                                        {" "}
                                        <cite title="Source Title">{detail.name}</cite>
                                    </footer>
                                </blockquote>
                            </div>
                        </div>
                        <span className="border border-primary "></span>
                    </div>
                ))}
            </div>);
    } 
} 
export default App;