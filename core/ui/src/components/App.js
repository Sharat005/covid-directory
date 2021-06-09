import React, { Component, Fragment } from 'react';
import ReactDOM from 'react-dom';
import Dashboard from './dashboard/dashboard';
import AddUserinfo from './userinfo/AddUserinfo';
import Screen from './screen/screen';

import Header from './layout/Header';

import { Provider } from 'react-redux';
import store from '../store';
import { Switch } from 'react-router';

class App extends Component {
    render() {
        return (
            <Provider store={store}>
                <Fragment>
                    <Header />
                    <div className="container">
                        {/* <nav>
                            <ul>
                                <li><a href="/dash">Manatee</a></li>
                                <li><a href="/add">Narwhal</a></li>
                                <li><a href="/screen">Whale</a></li>
                            </ul>
                        </nav>
                        <BrowserRouter>
                            <Switch>
                                <Route path="/dash">
                                    <Dashboard />
                                </Route>
                                <Route path="/add">
                                    <AddUserinfo />
                                </Route>
                                <Route path="/screen"> */}
                                    <Screen />
                                {/* </Route>
                            </Switch>
                        </BrowserRouter> */}
                    </div>
                </Fragment>
            </Provider>
        )
    }
}

ReactDOM.render(<App />, document.getElementById("app"));