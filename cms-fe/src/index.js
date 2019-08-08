import React from 'react';
import ReactDOM from 'react-dom';

class Cms extends React.Component {
	componentDidMount() {
		this.getStudents();
	}

	getStudents() {
		fetch('http://localhost:8000/students/')
			.then((results) => results.json())
			.then((results) => console.log(results));
	}

	render() {
		return null;
	}
}

ReactDOM.render(<Cms />, document.getElementById('root'));
