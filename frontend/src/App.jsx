import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import MedicalPage from './pages/MedicalPage';
import CropPage from './pages/CropPage';
import NewPage1 from './pages/NewPage1';
import NewPage2 from './pages/NewPage2';

function App() {
    return (
        <Router>
            <Switch>
                <Route path="/medical" component={MedicalPage} />
                <Route path="/crop" component={CropPage} />
                <Route path="/newpage1" component={NewPage1} />
                <Route path="/newpage2" component={NewPage2} />
            </Switch>
        </Router>
    );
}

export default App;
