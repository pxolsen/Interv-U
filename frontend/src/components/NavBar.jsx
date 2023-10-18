import * as React from "react";
import AppBar from "@mui/material/AppBar";
import {
  Avatar,
  Link,
  Toolbar,
  Typography,
  Input,
  useTheme,
} from "@mui/material";

const linkStyle = {
  textDecoration: "none",
  color: "inherit", // Inherit text color from parent
  "&:hover": {
    textDecoration: "underline", // Add underline on hover
  },
};

function NavBar() {
  const theme = useTheme();
  return (
    <AppBar>
      <Toolbar>
        <Link href="/" style={linkStyle}>
          <Typography variant="h6" sx={{ marginRight: theme.spacing(2) }}>
            Interv-U
          </Typography>
        </Link>
        <Link href="/questions" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(2) }}
          >
            Questions
          </Typography>
        </Link>
        <Link href="/answers" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(2) }}
          >
            Answers
          </Typography>
        </Link>
        <Link href="/profile" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(2) }}
          >
            Profile
          </Typography>
        </Link>
        <Input
          sx={{ marginLeft: "auto", bgcolor: "white" }}
          placeholder="Search"
        />
        <Avatar sx={{ marginLeft: theme.spacing(2) }} />
      </Toolbar>
    </AppBar>
  );
}
export default NavBar;
