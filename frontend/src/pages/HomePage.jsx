import { Box, Button, Container, Grid, Typography, useTheme } from "@mui/material";
import ImageCarousel from "../components/ImageCarousel";

function HomePage() {
    const theme = useTheme();
  return (
    <>
      <Box
        // mt={"xs"}
        height={"100vh"}
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        padding={theme.spacing(2)}
      >
        <Box maxWidth={"lg"}>
          <Typography
            variant="h2"
            sx={{ mb: 2, textAlign: "center" }}
          >
            Interv-U
          </Typography>
          <Typography
            variant="h5"
            sx={{ textAlign: "center", mb: 2 }}
          >
            Your one-stop shop for acing the behavioral interview
          </Typography>
          <Button
            variant="contained"
            color="primary"
            sx={{ display: "block", margin: "0 auto", mb:2 }}
          >
            Get Started!
          </Button>
        </Box>
        <Box maxHeight={"50vh"}>
        <ImageCarousel />
        </Box>
      </Box>
    </>
  );
}

export default HomePage;
