import {
  Box,
  Button,
  Container,
  Grid,
  Typography,
  useTheme,
  useMediaQuery,
} from "@mui/material";
import ImageCarousel from "../components/ImageCarousel";

function HomePage() {
  const theme = useTheme();
  const isLargeScreen = useMediaQuery(theme.breakpoints.down("lg"));
  const isMedScreen = useMediaQuery(theme.breakpoints.down("md"));
  return (
    <Grid container>
      <Grid item xs={12} lg={6}>
        <Box
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
          height="100vh"
          padding={theme.spacing(2)}
        >
          <Typography variant="h2" sx={{ mb: 2, textAlign: "center" }}>
            Interv-U
          </Typography>
          <Typography variant="h5" sx={{ textAlign: "center", mb: 2 }}>
            A better way to prepare for the behavioral interview
          </Typography>
          <Button
            variant="contained"
            color="primary"
            sx={{ display: "block", margin: "0 auto", mb: 2 }}
          >
            Get Started
          </Button>
        </Box>
      </Grid>
      <Grid item xs={12} lg={6}>
        <Box
          display="flex"
          flexDirection="column"
          alignItems="center"
          justifyContent="center"
          height="100vh"
          padding={theme.spacing(2)}
        >
          <ImageCarousel />
        </Box>
      </Grid>
    </Grid>
  );
}

export default HomePage;
