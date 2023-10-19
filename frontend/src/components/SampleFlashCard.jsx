import { Button, Paper, Typography, Input, Box } from "@mui/material";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";

function SampleFlashCard() {
  return (
    <Paper
      sx={{ height: "395px", justifyContent: "center", alignItems: "center" }}
    >
      <Box display="flex" justifyContent="space-between" alignItems="center" marginBottom={2}>
        <Button variant="outlined" sx={{ fontWeight: "bold" }}>
          Answered
        </Button>
        <Button variant="outlined" sx={{ fontWeight: "bold" }}>
          Liked
        </Button>
      </Box>
        <Typography variant="h5" sx={{ mb: 5 }}>
          "Can you tell me about the last project you worked on and some of the
          challenges you experienced along the way?"
        </Typography>
      <Accordion sx={{ ml: 2, mr:2}}>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          //   aria-controls="panel1a-content"
          //   id="panel1a-header"
        >
          <Typography sx={{ fontWeight: "bold" }}>Answer It</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Input sx={{ width: "100%", ml:2, mr:2 }} />
        </AccordionDetails>
      </Accordion>
      <Box display="flex" justifyContent="space-between" alignItems="center">
      <Button variant="contained" sx={{ mr: 1, ml:1 }}>
        Like
      </Button>
      <Button variant="contained">Save</Button>
      <Button variant="contained" sx={{ ml: 1, mr:1 }}>
        Seen
      </Button>
      </Box>
    </Paper>
  );
}
export default SampleFlashCard;
