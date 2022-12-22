import "./style.css";
import init, { greet } from "innards";

init().then(() => {
    greet();
});
