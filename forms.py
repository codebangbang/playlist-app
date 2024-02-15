"""Forms for playlist app."""

from wtforms import SelectField, StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional

class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Playlist Name", validators=[InputRequired(message="Playlist Name can't be blank")])
    description = StringField("Description", validators=[Optional()])
    submit = SubmitField('Add Playlist')
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField("Song Title", validators=[InputRequired(message="Song Title can't be blank")])
    artist = StringField("Artist", validators=[InputRequired(message="Artist Name can't be blank")])
    submit = SubmitField('Add Song')
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
