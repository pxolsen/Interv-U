import * as React from "react";
import AppBar from "@mui/material/AppBar";
import {
  Avatar,
  Link,
  Toolbar,
  Typography,
  Input,
  useTheme,
  useMediaQuery,
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
  const isSmallScreen = useMediaQuery(theme.breakpoints.down('sm'));
  const isMedScreen = useMediaQuery(theme.breakpoints.down('md'));
  return (
    <AppBar>
      <Toolbar>
        <Link href="/" style={linkStyle}>
          <Typography variant="h5" sx={{ marginRight: theme.spacing(5), fontWeight: "bold", ml:3 }}>
            Interv-U
          </Typography>
        </Link>
        {isSmallScreen ? null : (
          <>
        <Link href="/questions" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(3) }}
          >
            Questions
          </Typography>
        </Link>
        <Link href="/answers" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(3) }}
          >
            Answers
          </Typography>
        </Link>
        {/* <Link href="/profile" style={linkStyle}>
          <Typography
            variant="subtitle1"
            sx={{ marginRight: theme.spacing(2) }}
          >
            Profile
          </Typography>
        </Link> */}
        </>
        )}
        {isMedScreen ? null : (
          <Input sx={{ bgcolor: 'white', pl:1 }} placeholder="Search" />
        )}
        <Avatar sx={{ marginLeft: "auto"}} />
      </Toolbar>
    </AppBar>
  );
}
export default NavBar;
